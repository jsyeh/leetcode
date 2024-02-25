# 題意：有一堆數字 nums，如果 nums[i], nums[j] 最大公因數>1 就可走動
# 題目問：「數字間能全部走完嗎？」也就是任兩數，都能「走到」
# 因 10^5 個數字太多了，無法「暴力」去試全部的可能，是 Hard 題
# 看了題目提供的 Hint 1: 每個數都「找出全部質因數」
# 
# 這題好難啊！我想的方法，會超過時間！改模仿 LeetCode 排名1 cpcs 的寫法
# 參考 cpcs 今天的 C++ 寫法，再翻譯成 Python
# https://leetcode.com/submissions/detail/1185309080/
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def getf(f, x): # 可找到 group 的祖先
            if f[x]==x: return x # 我就是祖先
            f[x] = getf(f, f[x]) # 不是祖先，就找到祖先，順便更新
            return f[x] # 回傳祖先
        def merge(f, num, x, y):
            x = getf(f, x) # 找到x的祖先
            y = getf(f, y) # 找到y的祖先
            if x==y: return # 若祖先相同，很好，不需merge
            if num[x] < num[y]: # 讓群組數量大的當祖先
                x, y = y, x # 現在 num[x] 比較大了
            f[y] = x # 設定好祖先：合併，設定y群的祖先是x
            num[x] += num[y] # 數量都集合到大的那群（x 那群）

        N = len(nums)
        if N==1: return True # 只有1個數，一定可走到，直接結束

        f = [i for i in range(N)] # 群的對照表，一開始 f[i] = i 自己一群
        num = [1]*N # 每一群都只有1個數，也就是只有「自己」
        have = {} # have[d] 是「質數d」對應的第1個數
        for i,x in enumerate(nums): # 逐一處理每個數
            if x==1: return False # 不幸遇到1，gcd(x,other)不可能>1,必失敗

            d = 2 # 質因數分解，先從2開始試
            while d*d<=x: # ex. 7*7=49, 49質因數只要測到7即可
                if x%d==0: # 若能整除，便是找到因數（可證明剛好是質因數）
                    if d in have: # 若出現過 d 這個質數
                        merge(f, num, i, have[d]) # 馬上合併 i 和 質數d 對應的頭
                    else: # 若沒出現過
                        have[d] = i # 記錄 質數d 對應的頭是 i
                    while x%d==0: x //= d # 趁機「一直除盡」
                d += 1 # 換試下一個數
            # 若非質數，前面會運作。
            # 但若剩下質數，再做下面處理（這是加速的技巧，省下大量時間）
            if x>1: # 前面會讓 x 越除越小，但「除完後若還有剩」那 x 就是質數
                if x in have: # 模仿前面的 merge
                    merge(f, num, i, have[x])
                else:
                    have[x] = i # 模仿前面的「記錄頭」
        return num[getf(f,0)] == N # 

# 今天這題，我用 Python 寫了好久、做好多加速，最後測到 case 918/928 累積超時
# 「累積」928個測資，我的Python程式(分段處理)不夠快，放棄原來的作法。
'''
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1: return True # 只有1個數，一定可走到

        prime = [] # 存「小於10^5」的全部的質數
        sieve = [True]*100001 # 利用篩子sieve來計算質數
        for i in range(2,100001):
            if sieve[i]: 
                prime.append(i)
                for k in range(i*i, 100001, i): # i*i開始殺
                    sieve[k] = False
        N = len(nums)
        visitedI = [False]*N # visitedI[i] 對應 nums[i] 有否走過
        visitedG = [True]*len(prime) # visitedG[g] 對應 prime group g 被用過
        factor = [[] for _ in range(N)] # factor[i] 存 nums[i] 的「全部質因數」
        group = [[] for _ in range(len(prime))] # 記錄 prime group g 裡，對應哪些 nums[i]

        @cache
        def compPrimeFactor(num):
            ans = []
            for g,p in enumerate(prime): # prime group g 對應 prime p
                if num%p==0: # 整除的質因數
                    ans.append(g)
                    #factor[i].append(g) # 記錄對應的 group i
                    #group[g].append(i) # 對應哪些 nums[i]
                    #visitedG[g] = False # 之後要確認「有參訪到它」
                    while num%p==0: num //= p
                if p>=num: return ans # 不用再除大的數，省下時間
            return ans

        for i,num in enumerate(nums): # 逐一計算「質因數」
            if num==1: return False # 如果不只1個數時，若有個數是1，無法 gcd(nums[i],nums[j])>1
            factors = compPrimeFactor(num)
            for g in factors:
                factor[i].append(g)
                group[g].append(i)
                visitedG[g] = False

        #print(factor[:10])
        #print(group[:10])
        # 天啊，10^5個 99991 光是質因數分解，就TLE超時
        # 因 99991是第9591個質數，計算就要10^9超時了
        
        # 接下來，只要有相同的質因數，就能算是同一國，可用BFS看group是否全能到達
        queue = deque() # 裡面放 nums[i] 的 i
        queue.append(i)
        while len(queue)>0:
            nowI = queue.popleft()
            if visitedI[nowI]==False:
                visitedI[nowI] = True
                for g in factor[nowI]: # 把對應的 group 加入處理
                    if visitedG[g]==False: 
                        visitedG[g] = True
                        for ii in group[g]:
                            if visitedI[ii]==False:
                                queue.append(ii)
        # 最後逐項檢查，看是否全部 visited過
        for v in visitedG:
            if v==False: return False
        return True
'''
# 小心測資 [1] 只有1個數，可走到
# 小心測資 [1,1] 因為 gcd(1,1)==1 無法互相走到
# case 764/925: [14,30,30,49]
# case 676/925: [52,98,42,72,60,96,30,91,42,60,70,35,60,40,70,42,70,42,24,70,15,35,75,75,90,90,70,70,77,78,30,70,66,78,42,30,90,70,90,60,70,15,66,10,15,70,77,30,12,65,70,14] 
# 如果「質因數分解」沒有效率，那累積的時間會超時
# case 916/925: 滿滿的99991 超大的質數 使用 @cache 加速
# case 918/925: 從100000,99999,99998,...,2,1 沒辦法加速

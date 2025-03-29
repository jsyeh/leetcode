# LeetCode 2818. Apply Operations to Maximize Score
# 每次「挑一段subarray」（最多n*(n+1)/2挑法）
# subarray 裡最高的 prime score（有幾個質因數）挑其中1個數，再把「那個數」乘起來，
# 經過 k 次操作，希望得到最高分數（因答案很大，要再取 10^9＋7 餘數）
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def modPow(x, y, m):  # x的y次方，再取m餘數，用「函式呼叫函式」快速解
            if y==0: return 1  # 任何數的0次方，是1
            ans = modPow(x, y//2, m) % m  # 拆解成「左右」兩半
            ans = (ans * ans) % m
            if y%2==1: return (ans * x) % m  # 奇數的話，要多乘一個 x
            return ans  # 偶數的話，就不用再乘一個 x
        MOD = 10**9+7  # 數字太大，要取餘數
        N, M = len(nums), max(nums)  # N 個數，最大的數是M
        prime = []  # 存放質數
        table = [True] * (M+1)  # 製作10萬以下的「質數對照表」
        for i in range(2,M+1):  # 用「篩子法」找質數
            if table[i] == True:  # 沒被篩掉的，是質數
                prime.append(i)  # 記錄在 prime 裡
                for kk in range(i*i, M+1, i):  # 「篩子法」把「質數」的倍數篩掉
                    table[kk] = False  # 因題目有 k 所以迴圈改用 kk
        pscore = [0] * N  # pscore[i] 對應 nums[i] 的「質因數個數」個數
        pfactor = defaultdict(int)  # pfactor[num] 對應 num 的質因數個數
        for i,num in enumerate(nums):  # 依序計算「質因數個數
            if num==1:
                pfactor[num] = pscore[i] = 0
                continue
            if table[num]==True:  # 剛好是質數
                pfactor[num] = pscore[i] = 1  # 「質因數個數」是 1
                continue  # 就不要再用 for 迴圈計算了
            if pfactor[num] != 0:  # 剛好有計算過
                pscore[i] = pfactor[num]  # 省下計算的時間
                continue
            for p in prime:
                if num == 1: break  # 剝皮法，把數字剝光了，就結束
                if num%p==0:  # 可整除
                    pscore[i] += 1  # 找到1個質因數
                    while num%p==0:
                        num //= p  # 就除掉它
            pfactor[nums[i]] = pscore[i]
        # 利用 monostack 建出 nums[i] 對應的 left[i] 及 right[i] 左右滑動的掌管範圍
        left, right = [0]*N, [0]*N  # 這裡模仿 Solutions 裡 Vlad 的解法
        score_l, score_r = [-1]*8, [N]*8  # Vlad 發現「質因數」最多只有7個
        for i in range(N):  # 從左到右，處理左界
            score = pscore[i]  # 現在這格的 pscore 值
            left[i] = max(score_l[score:])  # 左界，是左邊「比它大」的最大邊
            score_l[score] = i  # 更新 score 目前對應的最右邊位置
        for i in range(N-1, -1, -1):  # 倒過來的迴圈，處理右界
            score = pscore[i]  # 現在這格的 pscore 值
            if score < 7: right[i] = min(score_r[score+1:])  # 更新「右界」
            score_r[score] = i  # 更新 score 目前對應的最左邊位置
        table = [(nums[i],pscore[i],i) for i in range(N)]  # 新對照表，值 vs. 質因數個數
        table.sort(reverse=True)  # 照「值高到低」排好
        ans = 1  # 挑「最大的數」，再看它能「左右展開」幾個「範圍」
        for x,p,i in table:  # 「值高到低」依序處理
            if k <= 0:  break  # 只要還剩下 k 次操作機會，就繼續做。但 k 耗盡，就離開
            # 往左滑、往右滑
            take = min( k, (i-left[i])*(right[i]-i) )  # 有幾種可能取法
            ans = (ans * modPow(x, take, MOD)) % MOD
            k -= take
        return ans

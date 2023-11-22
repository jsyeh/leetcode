# 這題超簡單，只要熟悉2D陣列 nums[i][j] 對應的位置在哪裡
# 口訣：左手i 右手j
# 另一個技巧，是斜線，對應其實就是 i+j==s (s會慢慢增加)
# 移項一下， j = s - i，也就是決定左手i的時候，瞬間算出右手j在哪裡
# 但是 i 的迴圈要從下往上 （題目的圖秀得很清楚）
# 最後，避開「缺的項」或是負的j就好了
# 但是上面的方法，不幸「會超時」Time Limit Exceeded 太慘了
#
# 所以，偷看Editorial的兩個答案，都看懂了，都很巧妙！！！
# 第一種方法，把對角線 i+j==s 照著 s 加到字典 dict 的裡面 groups[s]
#   在加到字典時，也照著「從下到上」的順序。最後 extended 整條插進去，搞定
# 第二種方法，利用 BFS 的技巧，取出 queue 的值，同時把它的左下角+右方再加入queue
#   就把答案算出來了
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 第一種方法，用字典，10行
        groups = defaultdict(list) # 依照 i+j 的值來分 groups
        maxS = 0 # 最大的斜線 i+j 的值
        for i in range(len(nums)-1, -1, -1): # 倒過來，往下往上的左手i
            for j in range(len(nums[i])):
                groups[i+j].append(nums[i][j]) # 從下到上，分group加入
                maxS = max(maxS, i+j) # 最大的斜線 i+j 的值
        # 以上把 groups字典都做好了，接下來「依序」插入ans
        ans = []
        # for s in groups: # 不能用這個迴圈，要用下面的迴圈
        for s in range(maxS+1): # s從0開始，逐條斜線去插入
            # print(s) # Debug 確認範圍
            ans.extend(groups[s]) # 整條插入
        return ans        
        

        '''
        # 第二種方法，用queue BFS，12行
        queue = deque() # BFS用的排隊
        queue.append((0,0))
        M = len(nums)
        ans = []
        while len(queue)>0: 
            i, j = queue.popleft();
            ans.append(nums[i][j])
            if j==0 and i<M-1: # (最左下角的那個)還能往下加
                queue.append( (i+1,j) )
            if j<len(nums[i])-1: # (每個人)還能往右加
                queue.append( (i,j+1) )
        return ans

        # 下面的方法，是我一開始直覺想到的，但它會超過時間
        M = len(nums) # 先知道「左手i」的範圍
        N = max(len(nums[i]) for i in range(M)) 
        # 右手j的範圍，最大長的。這行其實是倒裝句，逐個nums[i]去取最大值
        # print( [len(nums[i]) for i in range(M)] ) # 印出，確認沒寫錯
        ans = [] # 放答案
        start1 = max( i+len(nums[i]) for i in range(M)) # 範圍也要再變小
        for s in range(start1):
        # for s in range(M+N): # 先決定「第幾條斜線」 i+j==s
            start2 = min(s, M-1) # 範圍倒著數的範圍
            for i in range(start2, -1, -1):
            # for i in range(M-1, -1, -1): # 從下到上的i
                j = s - i # 用前面移項的公式，決定右手j
                if j<0 or j>=len(nums[i]): continue # 避開「缺項」

                # print(i, j, nums[i][j]) # Debug用，確認順序正確
                ans.append(nums[i][j]) # 把答案加入
        return ans # 開心
        '''
# case 52/56: 有滿滿的測試資料時，for迴圈會 10^5 * 10^5 太慢，要加速

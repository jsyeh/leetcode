# LeetCode 2392. Build a Matrix With Conditions
# 有個 k * k 的矩陣，裡面剛好有 1...k 個數字，及一堆 0
# 給你 1...k 這些數字 在 row 的相對關係、在 col 的相對關係，要組合出矩陣。
# 若失敗(ex.存在 cycle 像 1->2 2->3 3->1) ，就回傳 empty matrix []
# 看了題目下方的 Hint 1: 利用 graph 關係 Hint 2: topological sort 找出順序
# 先用 topo sort 找到直向的順序、橫向的順序 (由最上面的 root 逐一解開), 再把數字填入矩陣中即可
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def helper(k, condition):  # 實作自己的 topological sort, 由 condition 算出可行的順序
            graph, inDegree = defaultdict(list), [0]*(k+1)  # 每個數字「後面有誰」、「inDegree前面幾個人」
            for a,b in condition: # 照著 a->b 的關係，
                graph[a].append(b)  # 更新 graph，也就是 a後面有b
                inDegree[b] += 1  # 更新 inDegree, 也就是 b 前面「又多1個人」
            # 做好準備（建好 graph 及 inDegree 資訊）後，建立 queue
            queue = deque()  # 要用 queue 進行 BFS
            for i in range(1, k+1):  # 將 inDegree 是 0 的 node 當成 BFS 之首
                if inDegree[i]==0: queue.append(i)
            ans = []  # 存放「排序後的結果」，希望在 matrix 裡「合理」的順序
            while queue:  # 只要 queue 還有內容，就繼續排
                a = queue.popleft()  # 現在處理 a
                ans.append(a)  # 放入 ans 的順序裡
                for b in graph[a]:  # a 後面有 b
                    inDegree[b] -= 1  # 因為處理完 a 所以 b 前面「少1人」
                    if inDegree[b]==0:  # # 只要==0(前面沒人) b就能加入queue
                        queue.append(b) # 就可以放入 queue 繼續處理
            return ans  # 處理完 queue 後，便找到完「某個方向」的答案了
        
        row = helper(k, rowConditions)
        col = helper(k, colConditions)
        if len(row)!=k or len(col)!=k: return []  # 不完整、有些點「無法排出來」，就失敗

        ans = [[0]*k for _ in range(k)] # k * k 矩陣裡，大部分是 0
        for now in range(1,k+1): # 針對 1...k 這些數字
            i, j = row.index(now), col.index(now) # 找到對應的 i,j 座標
            ans[i][j] = now # 將數字 放入 對應的 i,j 座標
        return ans

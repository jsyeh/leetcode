# LeetCode 2658. Maximum Number of Fish in a Grid
# grid[i][j] 代表水中「魚的數量，0代表陸地。問漁夫在同一片水中，最多得多少魚？
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def findFish(i,j):  # 從(i,j)出發捕魚，用「函式呼叫函式」的 DFS 解題
            ans = 0
            stack = [(i,j)]  # 這個版本，使用 DFS 的 stack 來實作
            while stack:
                i,j = stack.pop()
                ans += grid[i][j]
                grid[i][j] = 0
                for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=ii<M and 0<=jj<N and grid[ii][jj]>0:
                        stack.append((ii,jj))
            return ans
        ans = 0  # 每片海域「最多」能捕到多少魚？
        for i in range(M):
            for j in range(N):
                if grid[i][j]>0: # 是水、有魚
                    now = findFish(i,j) # 從(i,j)出發捕魚，能得到多少魚？
                    ans = max(ans, now)  # 更新答案
        return ans

# LeetCode 1219. Path with Maximum Gold
# 金礦 grid[i][j] 有不同數量的 gold 可開採, 可從任意地方開始, 一格格開採
# 不能走到 gold為0的格子。問最多能得到多少金礦。看起來用 DFS 就可以解決了。
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= M or j >= N:
                return 0
            if grid[i][j] == 0:
                return 0  # 不能走到0的格子
            gold_here = grid[i][j]  # 這格有 gold_here 的金礦可採
            grid[i][j] = 0
            ans1 = dfs(i + 1, j)  # 往4個方向, 都試過一次
            ans2 = dfs(i - 1, j)
            ans3 = dfs(i, j + 1)
            ans4 = dfs(i, j - 1)
            grid[i][j] = gold_here  # 離開這輪時, 把 gold 放回去
            return gold_here + max(ans1, ans2, ans3, ans4)  # 用最大值
        ans = 0
        for i in range(M):
            for j in range(N):
                ans = max(ans, dfs(i, j))
        return ans

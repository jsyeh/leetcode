# 這題用簡單的 DFS 便能把「能走到的」都走到了！
# 改用「函式呼叫函式」來做
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # 了解長寬
        visited = [[False]*N for _ in range(M)] #走過不再走
        def visiting(i, j)->int:
            if i<0 or j<0 or i>=M or j>=N or visited[i][j] or grid[i][j]==0:
                return 0 # 超過範圍、走過、不能走，都略過
            visited[i][j] = True
            ans = 1 + visiting(i+1,j) # 本身能來，就是1
            ans += visiting(i-1,j) # 要往4個方向測試
            ans += visiting(i,j+1)
            ans += visiting(i,j-1)
            return ans

        maxAns = 0
        for i in range(M): # 左手i
            for j in range(N): # 右手j
                maxAns = max(maxAns, visiting(i,j))
        return maxAns

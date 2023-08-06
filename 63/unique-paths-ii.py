class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        table = [[0]*N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if grid[i][j]==1: table[i][j] = 0
                elif i==0 and j==0: table[i][j] = 1
                elif i==0: table[i][j] = table[i][j-1]
                elif j==0: table[i][j] = table[i-1][j]
                else: table[i][j] = table[i-1][j] + table[i][j-1]
        return table[M-1][N-1]

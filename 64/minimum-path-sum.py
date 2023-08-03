class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # 在一行內設定兩個變數，只是想少一行
        table = [[0]*N for _ in range(M)] # 建二維陣列 table[i][j] 表示minPathSum

        table[0][0] = grid[0][0] # 最左上角那一格，下面則是左邊、上邊的格子
        for i in range(1,M): table[i][0] = table[i-1][0] + grid[i][0]
        for j in range(1,N): table[0][j] = table[0][j-1] + grid[0][j]

        for i in range(1,M):
            for j in range(1,N):
                table[i][j] = grid[i][j] + min(table[i-1][j], table[i][j-1])
        # print(table)
        return table[M-1][N-1]

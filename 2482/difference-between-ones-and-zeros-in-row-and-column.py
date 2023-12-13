# 題目看起來很簡單，就是把 row One + col One - row Zero - col Zero
# 不過迴圈要寫得有技巧一點，不然會超時
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        oneRow, zeroRow = [0]*M, [0]*M # 先用來統計有多少zero
        oneCol, zeroCol = [0]*N, [0]*N # 先用來統計有多少zero
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    oneRow[i] += 1
                    oneCol[j] += 1
                else:
                    zeroRow[i] += 1
                    zeroCol[j] += 1
        diff = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N): # 接下來照著題目的公式，把答案算出來
                diff[i][j] = oneRow[i] + oneCol[j] - zeroRow[i] - zeroCol[j]
        return diff

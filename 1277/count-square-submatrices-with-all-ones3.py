# LeetCode 1277. Count Square Submatrices with All Ones
# 在 matrix 裡，有0有1，問「有幾種正方形」裡面「全塞滿1」
# 典型 Dynamic Programming 題目，很像 2348. Number of Zero-Filled Subarrays
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])  # 先知道 matrix 的長寬
        # 使用 Bottom-Up Dynamic Programming，建表格「慢慢更新」
        combo = [[0]*(N+1) for i in range(M+1)]
        # combo[i+1][j+1] 對應 到 matrix[i][j] 結束，累積「全塞滿1」正方形有幾個
        comboRow = [[0]*(N+1) for i in range(M+1)]
        # comboRow[i][j+1] 對應 到 matrix[i][j] 結束，累積「橫向」連續1有幾個
        comboCol = [[0]*(N+1) for i in range(M+1)]
        # comboCol[i+1][j] 對應 到 matrix[i][j] 結束，累積「直向」連續1有幾個
        ans = 0
        for i in range(M):  # 針對每個小格子
            for j in range(N):
                if matrix[i][j]==1:  # 如果這個小格子是1
                    r = comboRow[i][j+1] = comboRow[i][j] + 1  # 累積「橫向」
                    c = comboCol[i+1][j] = comboCol[i][j] + 1  # 累積「直向」
                    combo[i+1][j+1] = min(combo[i][j]+1, r, c)
                    # 累積「以i,j結尾」的正方形數目，用combo[i][j]延伸
                    # 但會受限 row i 和 col j 的長度，所以用 min() 來更新
                    ans += combo[i+1][j+1]  # 很像 2348 這題的作法
        return ans

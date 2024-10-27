# LeetCode 1277. Count Square Submatrices with All Ones
# 在 matrix 裡，有0有1，問「有幾個正方形」裡面都是1
# 典型的 DP 題目，把大問題，拆解成小問題：如果建表格，裡面存「正方形的最大數量」
# 沒想到這題只有300x300這麼小，用暴力3層for迴圈，竟然也解得出來（題目Hint 1 & Hint 2就是建議這個「很慢」的方法）
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])  # 先了解 matrix 長寬
        # table = [[matrix[i][j] for j in range(N)] for i in range(M)] # 建出表格（也可重覆利用matrix)
        areaSum = [[0]*(N+1) for _ in range(M+1)]  # 每格會存「左上角」加起來的值
        for i in range(1,M+1):  # 完整建出 area sum table 以便快速找出「某個長方形」裡有「幾個1」
            for j in range(1,N+1): 
                areaSum[i][j] = matrix[i-1][j-1] + areaSum[i-1][j] + areaSum[i][j-1] - areaSum[i-1][j-1]
        ans = 0
        for i in range(1,M+1):
            for j in range(1,N+1): 
                for s in range(1, min(i,j)+1):  # 正方形的大小，「暴力3層for迴圈」很慢，但可以正確
                    if areaSum[i][j] - areaSum[i][j-s] - areaSum[i-s][j] + areaSum[i-s][j-s] == s*s:
                        ans += 1  # 上面神秘的公式，能快速找到 i,j往左上角（大小為s的）正方形裡，有幾個1，剛好s*s就是全塞滿1
        return ans


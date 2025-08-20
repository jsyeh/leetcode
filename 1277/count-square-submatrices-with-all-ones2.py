# LeetCode 1277. Count Square Submatrices with All Ones
# 在 matrix 裡，有0有1，問「有幾種正方形」裡面「全塞滿1」
# 1x1 是正方型、2x2 也是正方形，好像還蠻簡單的。但太多層迴圈會超時。
# 想到在「影像處理」有「積分影像(Integral Image)」的技巧，「0,0開始的長方形」累積的值，剛好可以用！
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])  # 先了解 matrix 長寬
        area = [[0]*(N+1) for _ in range(M+1)]  # 每格存「左上大方塊」加總
        for i in range(1,M+1):  # 建出 area sum 可快速找出「某個方形」裡「有幾個1」
            for j in range(1,N+1): 
                # area[i][j] 對應 matrix[0][0] 到 matrix[i-1][j-1] 的長方形裡「有幾個1」
                area[i][j] = matrix[i-1][j-1] + area[i-1][j] + area[i][j-1] - area[i-1][j-1]
                #            現在新加的這格     +上方「左上大方塊」+左方「左上大方塊」-左上「左上大方塊」
        ans = 0
        for i in range(1,M+1):  # 左手i
            for j in range(1,N+1):  # 右手j
                for s in range(1, min(i,j)+1):  # 正方形邊長s，「暴力3層for迴圈」很慢，但正確
                    if area[i][j] - area[i][j-s] - area[i-s][j] + area[i-s][j-s] == s*s:
                    # 神秘的公式，能快速找到 i,j往左上角（邊長s）正方形裡，有幾個1。剛好「全塞滿1」是s*s
                        ans += 1  # 又找到「全塞滿1」的正方形
        return ans

# LeetCode 11. Sparse Matrix Multiplication
# 就做「矩陣乘法」，兩矩陣裡，有很多0。這題若直接照著模擬，速度會慢。
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M, K, N = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0] * N for _ in range(M)]
        for i in range(M):
            for k in range(K):  # 調一下迴圈的順序
                if mat1[i][k]==0: continue  # 避開有0的項，速度就變快了!
                for j in range(N):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans

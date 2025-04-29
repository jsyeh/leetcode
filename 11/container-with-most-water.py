# LeetCode 11. Sparse Matrix Multiplication
# 就做「矩陣乘法」，兩矩陣裡，有很多0。這題直接照著模擬，就可以做出來了，不過速度慢。
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M, K, N = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                for k in range(K):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans

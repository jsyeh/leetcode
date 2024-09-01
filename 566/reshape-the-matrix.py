# LeetCode 566. Reshape the Matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        if M*N != r*c: return mat  # 面積不同、無法正確對應，回傳舊的矩陣

        ans = [[0]*c for _ in range(r)] # 準備好
        for i in range(r):
            ans.append([])  # 
            for j in range(c):
                ii, jj = (i*c+j)//N, (i*c+j)%N
                ans[i][j] = mat[ii][jj]
        return ans

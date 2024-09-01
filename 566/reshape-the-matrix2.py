# LeetCode 566. Reshape the Matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        if M*N != r*c: return mat  # 面積不同、無法正確對應，回傳舊的矩陣

        ans = []  # 答案塞在裡面
        for i in range(r):
            ans.append([])  # 每個 row 一開始是空的 []
            for j in range(c):
                ii, jj = (i*c+j)//N, (i*c+j)%N
                ans[i].append(mat[ii][jj])  # 增加 row 的內容
        return ans

# LeetCode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# 找到「最大的正方形」加總 <= threshold，可用 prefix 陣列「快速找總和」再用 binary search
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M, N = len(mat), len(mat[0])  # 長、寬
        pre = [[0]*(N+1) for i in range(M+1)]  # prefix sum 陣列
        for i in range(M):
            for j in range(N):  # 更新 prefix sum 陣列
                pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
        def helper(s):  # 利用函式，判斷「邊長s的正方形」加總「有沒有機會<=threshold」
            for i in range(M-s+1): 
                for j in range(N-s+1):
                    if pre[i+s][j+s]-pre[i][j+s]-pre[i+s][j]+pre[i][j] <= threshold:
                        return -1  # 有機會，回傳 -1
            return 1  # 沒有機會，回傳 +1
        # 用 binary search 想找到「-1....-1 +1 +1」的 0 的位置，也就是合格的「最大正方形」
        return bisect_left(range(1,min(M,N)+1), 0, key=helper)

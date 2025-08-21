# LeetCode 1504. Count Submatrices With All Ones
# 數一數，有幾個 submatrix 方型的小矩陣，裡面都是1
# 題目 Hints 可使用 3 層迴圈 O(n^3) 的作法，依序累積更新答案
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        combo = [[0]*(N+1) for i in range(M)]
        ans = 0
        for i in range(M):
            for j in range(N):
                if mat[i][j]==1:
                    combo[i][j+1] = combo[i][j] + 1
                    now = combo[i][j+1]
                    for k in range(i, -1, -1):
                        now = min(now, combo[k][j+1])
                        ans += now
        return ans

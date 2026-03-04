# LeetCode 1582. Special Positions in a Binary Matrix
# 有幾個格子「本身是1」 而且「在row裡是唯一、在col裡是唯一」
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])  # 先知道格子的「長、寬」
        row = [0]*M  # 有 M 個 row，想知道「每個row」裡有幾格是1
        col = [0]*N  # 有 N 個 col，想知道「每個col」裡有幾格是1
        for i in range(M):  # 逐格統計
            for j in range(N):
                if mat[i][j]==1:  # 若某格是1
                    row[i] += 1  # 對應的 row i 多1個1
                    col[j] += 1  # 對應的 col j 多1個1
        ans = 0  # 再巡一次，想知「有幾格」本身是1，且在 row col 都唯一
        for i in range(M):
            for j in range(N):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    ans += 1  # 本身是1，且在 row col 都唯一
        return ans

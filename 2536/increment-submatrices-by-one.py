# LeetCode 2536. Increment Submatrices by One
# n x n 矩陣裡「都是0」，每次queries[i] 將 [r1,c1,r2,c2] 範圍「都加1」問最後矩陣的值
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [ [0]*(n+1) for i in range(n+1) ]  # 先做出「差異量」diff 矩陣
        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                diff[r][c1] += 1  # 記下「加1」的開始位置
                diff[r][c2+1] -= 1  # 在結束位置右邊「還原」
        ans = [[0]*n for i in range(n)]  # 最後的答案
        for i in range(n):
            now = 0  # 開始「累積」差異量
            for j in range(n):
                now += diff[i][j]  # 套用「差異量」
                ans[i][j] = now  # 存入答案的矩陣
        return ans

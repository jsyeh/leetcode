# LeetCode 2352. Equal Row and Column Pairs
# n x n 矩陣裡有幾組 (r,c) 對應 row[r] == col[c]
# 可先建出 row[i] 對應的「tuple」，用 Counter 記起來，再用 col[j] tuple去比較、累積出答案
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter()  # 累積 row 的 tuple 出現次數
        for row in grid:  # 逐一將各個 row 的 tuple
            counter[tuple(row)] += 1  # 累積對應 counter

        N = len(grid)
        grid2 = [[grid[j][i] for j in range(N)] for i in range(N)]  # i,j倒過來
        ans = 0  # 累積答案
        for col in grid2:  # grid2 的 row 對應 grid 的 col
            ans += counter[tuple(col)]  # col 對應「幾個相同內容的row」
        return ans

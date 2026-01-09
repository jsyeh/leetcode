# LeetCode 2352. Equal Row and Column Pairs
# n x n 矩陣裡有幾組 (r,c) 對應 row[r] == col[c]
# 可先建出 row[i] 對應的「tuple」，用 Counter 記起來，再用 col[j] tuple去比較、累積出答案
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter()
        ans = 0
        for row in grid:
            counter[tuple(row)] += 1
        for row in zip(*grid):
            ans += counter[tuple(row)]
        return ans

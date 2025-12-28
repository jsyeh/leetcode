# LeetCode 1351. Count Negative Numbers in a Sorted Matrix
# Easy 題：請問 grid[i][j] 裡，有幾個「負數」？
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 因「左右排好、上下也排好」能不能找到 O(M+N) 的解法呢？
        ans = 0  # 方法二
        M, N = len(grid), len(grid[0])
        i, j = 0, N-1
        while i<M:
            if j>=0 and grid[i][j]<0:  # 往左走
                j -= 1
            else:  # 往下走
                ans += N - j - 1  # 往下走時，收成「負數」的數量
                i += 1
        return ans

# LeetCode 1351. Count Negative Numbers in a Sorted Matrix
# Easy 題：請問 grid[i][j] 裡，有幾個「負數」？
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0  # 因為「數字很少」用暴力法「兩層迴圈」就可以成功
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0: ans += 1
        return ans

# LeetCode 3634. Minimum Removals to Balance Array
# nums 陣列「要刪掉幾個數」後，最大值 <= 最小值 * k
# 有人想到用 sliding window 的解法
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        N = len(nums)  # 有 N 個數字
        nums.sort()  # 將數字「小到大」排好
        ans = N - 1  # 最差的狀況，會刪 N-1 個數（剩1個）
        left = 0  # 左邊放在 0，之後會被往右拉
        for right in range(N):  # 決定「右邊最大值」的位置
            if nums[left] * k < nums[right]:  # 右邊超過範圍
                left += 1  # 左邊「就被往右拉」，對應「出問題」的數量
        return left  # 「出問題」的數量，就是要刪除的數量

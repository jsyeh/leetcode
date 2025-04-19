# LeetCode 2563. Count the Number of Fair Pairs
# 若 lower <= nums[i] + nums[j] <= upper 叫 fair pair，總共有多少組？
# 直覺用2層for迴圈，但 nums 有 10^5 太大，不能用2層迴圈。
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() # Hint 1 建議 sort() 因 sort 後的結果一樣多組
        # 再來就簡單了，用 for 迴圈，決定右邊界，再binary search看左邊的範圍
        ans = 0
        for i in range(1, len(nums)):  
            # 修改 binary search 的參數，不要用 nums[:i]即加速
            j_left = bisect_left(nums, lower - nums[i], hi = i)
            j_right = bisect_right(nums, upper - nums[i], hi = i)
            ans += j_right - j_left
        return ans


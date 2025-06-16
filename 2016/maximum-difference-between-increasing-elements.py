# LeetCode 2016. Maximum Difference Between Increasing Elements
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        left = nums[0]
        for i in range(len(nums)):
            ans = max(ans, nums[i]-left)
            left = min(left, nums[i])
        return -1 if ans==0 else ans

# LeetCode 908. Smallest Range I
# 挑 nums[i] += x 其中 -k <= x <= k，最後目標是 max(nums) - min(nums) 最小
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        if diff<2*k: return 0
        return diff - 2*k

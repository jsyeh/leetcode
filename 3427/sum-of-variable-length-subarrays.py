# LeetCode 3427. Sum of Variable Length Subarrays
# 從 max(0,i-nums[i]) ... i 一直加起來
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = [sum(nums[max(0,i-nums[i]):i+1]) for i in range(len(nums))]
        return sum(ans)

# LeetCode 3423. Maximum Difference Between Adjacent Elements in a Circular Array
# 陣列中，兩兩相鄰的數「最大的距離」
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            ans = max(ans, abs(nums[i-1] - nums[i]))
        return ans

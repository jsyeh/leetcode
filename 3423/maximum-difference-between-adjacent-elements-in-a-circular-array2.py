# LeetCode 3423. Maximum Difference Between Adjacent Elements in a Circular Array
# 陣列中，兩兩相鄰的數「最大的距離」
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # 使用倒裝句、配合 max() 的寫法
        return max( [abs(nums[i]-nums[i-1]) for i in range(len(nums))] )

        # 或另一種寫法，用 for 迴圈慢慢更新
        ans = -1
        for i in range(len(nums)):
            ans = max(ans, abs(nums[i-1] - nums[i]))
        return ans

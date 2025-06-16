# LeetCode 2016. Maximum Difference Between Increasing Elements
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans, left = -1, nums[0]  # 分別對應「答案」及目前「左邊最小的數」
        for i in range(len(nums)):  # 只用1層迴圈，就能解掉這題，更快
            if nums[i] > left:  # 因為 nums[i] 只與「左邊最小的數」比較
                ans = max(ans, nums[i]-left)  # 再更新答案
            left = min(left, nums[i])  # 更新「左邊最小的數」
        return ans

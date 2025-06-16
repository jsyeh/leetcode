# LeetCode 2016. Maximum Difference Between Increasing Elements
# nums 陣列裡，左邊 nums[i] < 右邊 nums[j] 時，請問「最大差多少」
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1  # 預設是 -1，代表沒有答案
        for i in range(len(nums)):  # 直覺使用「兩層迴圈」左手 i
            for j in range(i+1, len(nums)):  # 右手 j
                if nums[i]<nums[j]: ans = max(ans, nums[j]-nums[i])
                # 如果「左邊小、右邊大」，而且「距離更大」就更新
        return ans

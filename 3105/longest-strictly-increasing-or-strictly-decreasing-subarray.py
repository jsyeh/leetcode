# LeetCode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# 持續增加 or 持續減少，最長的長度是多少？
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]: inc += 1  # 增加
            else: inc = 1  # 沒有增加

            if nums[i-1] > nums[i]: dec += 1  # 減少
            else: dec = 1  # 沒有減少
            
            ans = max(ans, inc, dec)  # 最長的長度
        return ans

# 策略：(1)不符合題目要求的作法，直接for迴圈找答案
# (2) 先利用 binary search 找到rotated 的交界點，再用 binary search 找值
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums[i] == target: return i
        return ans

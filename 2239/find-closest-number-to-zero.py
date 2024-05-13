# 找到「最接近0」的數
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]  # 先隨便挑個數，當答案
        for num in nums:
            if abs(ans) > abs(num) or (abs(ans) == abs(num) and num > ans):
                ans = num
        return ans


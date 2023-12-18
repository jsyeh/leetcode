# 希望找到4個數字，使得 (a*b) - (c*d) 的值最大。
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2] - nums[0]*nums[1]

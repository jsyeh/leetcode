# LeetCode 136. Single Number
# nums 陣列裡「有1個數」只出現1次，找出來 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for c in counter:
            if counter[c]==1: return c

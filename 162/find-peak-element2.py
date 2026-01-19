# LeetCode 162. Find Peak Element
# 全部巡一次，就可找到任一個 peak element
# 不過題目希望用 O(log n) 找到。任一個local maximum 就可以。可用斜率法來做
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ansI = 0
        for i in range(len(nums)):
            if nums[i] > nums[ansI]: ansI = i
        return ansI

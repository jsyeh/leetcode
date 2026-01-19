# LeetCode 162. Find Peak Element
# 全部巡一次，就可找到任一個 peak element
# 不過題目希望用 O(log n) 找到。任一個local maximum 就可以。可用斜率法來做
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if nums[0]>nums[1]: return 0  # 最左邊「剛好」是 local max
        def helper(i):
            return nums[i-1] - nums[i]
        return bisect_left(range(len(nums)), 0, key=helper)-1

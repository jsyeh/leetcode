# LeetCode 1150. Check If a Number Is Majority Element in a Sorted Array
# 確認一下 target 是不是 nums 陣列裡「出垷次數」「過半」
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counter = Counter(nums)
        return counter[target] > len(nums)//2

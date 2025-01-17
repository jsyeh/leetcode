# LeetCode 1708. Largest Subarray Length K
# 將 nums 做出一堆「長度為k」的子陣列，（逐位比較）找出最大的子陣列
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # 因「每個數都不同」，只要比「每個」子陣列的「第一個數」找最大即可
        ansI = 0
        for i in range(len(nums)-k+1):  # 逐一比「每個」子陣列
            if nums[i] > nums[ansI]:
                ansI = i
        return nums[ansI:ansI+k]

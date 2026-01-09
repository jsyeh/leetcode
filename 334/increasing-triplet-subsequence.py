# LeetCode 334. Increasing Triplet Subsequence
# 是否能挑出 i<j<k 使得 nums[i] < nums[j] < nums[k]?
# 從左到右，先找到「最小值」，再找到「中間值」，找到比「中間值」大的數，即成功
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = mid = inf
        for num in nums:
            if num < low: low = num
            elif num>low and num < mid: mid = num
            elif num > mid: return True
        return False

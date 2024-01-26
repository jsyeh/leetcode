# 可以用 2 points 來做，不過改成 set 可能更簡單
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))

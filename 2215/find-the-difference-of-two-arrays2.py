# LeetCode 2215. Find the Difference of Two Arrays
# 找到2個陣列裡「不同的數」
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return list(s1-s2), list(s2-s1)

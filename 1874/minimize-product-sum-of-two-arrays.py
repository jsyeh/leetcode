# LeetCode 1874. Minimize Product Sum of Two Arrays
# 你可調整陣列裡的順序，讓「對應項相乘」加起來最小
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        return sum([nums1[i]*nums2[i] for i in range(len(nums1))])

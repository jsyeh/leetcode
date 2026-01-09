# LeetCode 2215. Find the Difference of Two Arrays
# 找到2個陣列裡「不同的數」
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans1 = []  # 在 nums1 裡、不在 nums2 裡
        for num in set1:
            if num not in set2: ans1.append(num)
        ans2 = []  # 在 nums2 裡、不在 nums1 裡
        for num in set2:
            if num not in set1: ans2.append(num)
        return [ans1, ans2]

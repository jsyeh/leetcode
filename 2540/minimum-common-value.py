# 問：nums1 和 nums2 裡面「相同」的數，最小是誰
# 因 nums1 和 nums2 都 sort() 過了，直接用 i, j 的 two pointers 即可解
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2) # 用來當 while 迴圈的上界
        i, j = 0, 0 # 兩個 pointers 針對 nums1[i] 和 nums2[j]
        while i<N1 and j<N2: # 若還沒超過範圍
            if nums1[i]==nums2[j]: return nums1[i] # 若相等，找到答案
            if nums1[i]>nums2[j]: j += 1 # 若左邊大，那右邊j +1
            else: i += 1 # 若右邊大，那左邊i +1
        return -1 # 沒找到答案

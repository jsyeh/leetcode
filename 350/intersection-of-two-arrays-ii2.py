# LeetCode 350. Intersection of Two Arrays II
# 兩個array裡，有哪些相同的部分？ 其實使用 Counter()就可解
# 也可以使用 sort()後，再逐一比對。
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort() # 這裡使用 sort 的方法來解
        nums2.sort() # 當兩個array都「從小到大」排序好後，就能「逐一比較
        i, j = 0, 0  # nums1[i] vs. nums2[j] 逐一比較
        ans = []
        while i<len(nums1) and j<len(nums2):  # 利用 while 迴圈，來模擬 for迴圈的樣子
            if nums1[i]==nums2[j]:  # 相同時
                ans.append(nums1[i])  # 就加入答案
                i, j = i+1, j+1  # 並將 i, j 一起進一格
            elif nums1[i]<nums2[j]: # 如果 nums1[i] 比較小
                i += 1  # 小的進一格
            else:  # 如果 nums2[j] 比較小
                j += 1  # 小的進一格
        return ans
        

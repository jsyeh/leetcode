# LeetCode 2570. Merge Two 2D Arrays by Summing Values
# nums1 和 nums2 裡，一堆「兩兩對應」的數字，對應項相同，可加起來。
# 最後再把對應項「小到大排好」，秀出一堆「兩兩對應」數字
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = Counter({a:b for a,b in nums1})
        ans += Counter({a:b for a,b in nums2})
        return sorted( [[a,b] for a,b in ans.items()] )
 

# LeetCode 2040. Kth Smallest Product of Two Sorted Arrays
# 兩個 sorted 陣列，要找到「乘起來第k小」的數。陣列很大，不能全部乘起來再排序
# 怎麼辦？ Hint 建議 binary search，那要怎麼「猜答案」呢？要用到2次 binary search!
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def helper(ans):  # nums1 乘 nums2 的數 <= ans 有幾個
            total = 0  # 乘出來的數，有幾個小於 ans 呢？
            for num1 in nums1:  # 左邊挑定 num1 再看 nums2 有幾個數配合
                if num1 < 0:  # 遇到負的，那 nums2 要從右邊挑
                    total += len(nums2) - bisect_left(nums2, ceil(ans/num1))
                elif num1 == 0:  # 挑到0, 太好了，只要 ans 是正的，就都加
                    if ans>=0: total += len(nums2)
                else:  # 遇到正的，那從左到右挑
                    total += bisect_right(nums2, floor(ans/num1))
            return total  # 最後「有幾個數<=ans」
        
        left, right = -10**10, 10**10
        while left < right:  # 第2次 binary 利用 left < right 就持續猜答案
            mid = (left+right) // 2
            if helper(mid) < k: left = mid + 1
            else: right = mid
        return left

# LeetCode 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
# 要把陣列裡的 0 都變成正數，且希望 sum(nums1) == sum(nums2) 最小
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zero1 = sum(nums1), nums1.count(0)  # 統計一下 目前總合 及 有幾個0
        sum2, zero2 = sum(nums2), nums2.count(0)
        # 最基礎款，可把 0 變成 1， 這時 sum1 += zero1 及 sum2 += zero2
        sum1 += zero1
        sum2 += zero2

        if sum1 == sum2: return sum1  # 如果剛好相同，就是答案
        if sum1 > sum2 and zero2>0: return sum1  # 左邊大、右邊小，右邊可以再加大
        if sum2 > sum1 and zero1>0: return sum2  # 右邊大、左邊小，左邊可以再加大
        return -1  # 以上機會都做不到，就沒辦法「加到相等」，失敗
        

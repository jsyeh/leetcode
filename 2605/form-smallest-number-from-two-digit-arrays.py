# LeetCode 2605. Form Smallest Number From Two Digit Arrays
# 從 nums1 和 nums2 各挑1個數，組合出的2位數「要最小」
# 或是 nums1 和 nums2 「共有」的最小的數
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        counter = Counter(nums1+nums2)  # 先統計數字出現次數
        for i in range(1,10):  # 從1到9巡，若出現2次，表示剛好都有，便是答案
            if counter[i]==2: return i
        # 若沒有共有的數，那就挑「最小的數」再組起來
        d1, d2 = min(nums1), min(nums2)
        if d1==d2: return d1
        elif d1<d2: return d1*10+d2
        else: return d2*10+d1

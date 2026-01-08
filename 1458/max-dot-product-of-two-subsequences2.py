# LeetCode 1458. Max Dot Product of Two Subsequences
# 將 nums1 nums2 挑出 subsequence 進行內積相乘相加，希望最大
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)  # 陣列的長度
        @cache
        def helper(i, j):  # 「函式呼叫函式」找到最大的內積
            if i==N1 or j==N2: return 0  # 終止條件：陣列結束
            # 可以相乘，也可不相乘
            ans1 = nums1[i]*nums2[j] + helper(i+1,j+1)
            ans2 = helper(i,j+1)
            ans3 = helper(i+1,j)
            return max(ans1, ans2, ans3)
        # 但直接 return helper(0,0) 在「答案是負的」會出錯
        # 針對「nums1全負、nums2全正」或「全正、全負」只會乘出負的
        if max(nums1) < 0 and min(nums2) > 0:  # 全負、全正
            return max(nums1) * min(nums2)  # 最接近0的負數
        if min(nums1) > 0 and max(nums2) < 0:  # 全正、全負
            return min(nums1) * max(nums2)  # 最接近0𥫩負數
        # 正常情況，則是用「函式呼叫函式」找到最大的內積
        return helper(0,0)

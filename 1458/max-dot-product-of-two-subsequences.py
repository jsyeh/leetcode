# 今天週末挑戰還是DP的Hard題。 helper(i,j)
# 因 maximum recursion depth 不能超過1000次，但長度已為500，麻煩了
# (原來是我的recursion條件有寫錯，修正OK)
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)

        @cache
        def helper(i, j)->int:
            if i==N1 or j==N2: return 0 # 只要有一邊超過，就不要再算了
            now = nums1[i] * nums2[j] + helper(i+1,j+1)
            return max(helper(i,j+1), helper(i+1,j), now)
        
        # 有個特殊狀況，是如果內積結果都是負的，只用helper()不能得到負值
        # 所以例外處理
        if max(nums1)<0 and min(nums2)>0: # 全負 vs. 全正
            return max(nums1)*min(nums2)
        if min(nums1)>0 and max(nums2)<0: # 全正 vs. 全負
            return min(nums1)*max(nums2)
        return helper(0,0)

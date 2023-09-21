# 希望 O(log(m+n)) 可使用 binary search
# 不過今天比較累，想偷懶，用O(m+n)暴力去找
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        if (M+N)%2==1:
            L = (M+N)//2
        else:
            L = (M+N)//2

        i1, i2, ans, ans2 = 0, 0, 0.0, 0.0
        while i1+i2<=L and i1<M and i2<N:
            if nums1[i1]<=nums2[i2]:
                ans2 = ans
                ans = nums1[i1]/1
                i1 += 1
            else:
                ans2 = ans
                ans = nums2[i2]/1
                i2 += 1
        if i1==M:
            while i1+i2<=L:
                ans2 = ans
                ans = nums2[i2]/1
                i2 += 1
        else:
            while i1+i2<=L:
                ans2 = ans
                ans = nums1[i1]/1
                i1 += 1
        if (M+N)%2==1:
            return ans
        else:
            return (ans+ans2)/2
        return ans

        '''
        left, right = 0, M
        while left<right:
            mid = (left+right)//2
            left2, right2 = 0, N
            target = M+N-mid
            while left2<right2:
                mid2 = (left2+right2)//2
                if nums1[mid]<nums2[mid2]:
                    left2
        '''
        

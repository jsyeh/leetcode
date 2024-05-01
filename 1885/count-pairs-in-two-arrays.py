# 左邊挑2個nums1[i]+nums1[j]，右邊2個對應項nums2[i]+nums2[j]加起來。
# 左邊要大。問有幾組 i,j
# 看了 votrubac 的文字解釋，覺得很帥！ 移項，變成 n1[i]-n2[i] + n1[j]-n2[j] > 0
# 再來 sort 後，會有妙用！
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(N)]
        a.sort()
        # 再來便可以 binary search, 找看 a[i] 右邊 a[j] 要配誰, 加整段
        ans = 0
        for i in range(N):  # 挑個 a[i]
            left, right = i + 1, N
            while left < right:  # binary search 找到 a[left]
                mid = (left + right) // 2
                if a[i] + a[mid] > 0:
                    right = mid
                else:
                    left = mid + 1
            ans += N - left  # left右邊全部都算成功
        return ans


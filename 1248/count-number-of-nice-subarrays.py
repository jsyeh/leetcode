# LeetCode 1248. Count Number of Nice Subarrays
# 連續的subarray裡，如果剛好有k個奇數，就是題目要的nice subarray
# 只要有不同的開頭、結尾，就是不同組，問「總共有幾組」nice subarrays
# 把問題化成另一個問題：「最多有k個奇數」的subarray數量
# 典型的 sliding window 題目，可以用伸縮自如的「毛毛蟲」來想像那個畫面
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    def atMost(self, nums, k): 
        N = len(nums)  # 陣列的長度
        ans = 0
        i, j = 0, 0  # j是左邊的尾巴，i是右邊的頭
        while j<=i and i<N: # 只要毛毛蟲還能爬
            if nums[i]%2==1: # 奇數
                k -= 1  # 用掉1個奇數
            i += 1 # 頭往右進，右不包含
            while k<0: # 用太多奇數、用過頭時，尾巴要吐出數字
                if nums[j]%2==1: 
                    k += 1  # 吐出奇數，可還原1個
                j += 1  # 尾巴往右縮
            ans += i-j+1 # i-j+1這段有k個奇數。
            # 這長度，對應「開頭在i」且「最多有k個奇數」的subarray有幾種可能
        return ans


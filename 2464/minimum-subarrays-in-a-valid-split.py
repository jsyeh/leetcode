# LeetCode 2464. Minimum Subarrays in a Valid Split
# nums 想拆成很多段 subarrays，其中每段的「頭尾」的最大公因數>1
# 請問「最少」能拆成「幾段」？
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        N = len(nums)
        @cache
        def helper(i):  # 從 nums[i] 往右「最少」能拆成「幾段」
            if i==N: return 0
            ans = inf
            # 最短的 subarray 可長度為1，所以迴圈從 i 開始
            for j in range(i, N):
                if gcd(nums[i], nums[j]) > 1:
                    # 函式呼叫函式
                    ans = min(ans, 1 + helper(j+1))
            return ans
            
        ans = helper(0)
        if ans==inf: return -1
        return helper(0)

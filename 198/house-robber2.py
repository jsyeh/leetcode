# LeetCode 198. House Robber
# 專業搶匪「不會連續搶2個相鄰的房子」，問「最多搶到多少錢」
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(i):  # 若從第i個房子開始搶，最多搶到多少錢
            if i>=len(nums): return 0  # 終止條件
            # 有兩種可能：搶nums[i]再避開鄰居 vs. 不搶、考慮 i+1
            return max(nums[i] + helper(i+2), helper(i+1))
        return helper(0)

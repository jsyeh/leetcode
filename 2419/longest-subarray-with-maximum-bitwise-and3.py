# LeetCode 2419. Longest Subarray With Maximum Bitwise AND
# bitwise AND 時，只要有任1個bit是0，那個bit就會變成0
# 所以要找 bitwise AND 的最大值，最好就「只有1個數」而且是最大的數。
# 如果換個題目講法，就變超簡單的題目：nums[i] 裡的最大值，「連續出現幾次？」
# 所以，先找到「最大值」，再用 for迴圈「巡」最多「連續出現的次數」就完成了。
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)  # 先找到最大值，當成目標
        combo, ans = 0, 0  # 目前「連續出現幾個target」 vs. 最多「連續出現幾個target」
        for num in nums:
            if num == target:  # 符合目標，太好了!
                combo += 1  # 又連續多了一個，真開心
                ans = max(ans, combo)  # 更新 ans
            else:
                combo = 0  # 重新從0個開始計算
        return ans

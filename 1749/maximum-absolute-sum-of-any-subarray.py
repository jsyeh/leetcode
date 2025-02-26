# LeetCode 1749. Maximum Absolute Sum of Any Subarray
# nums 裡，有一堆數，希望找到「某段subarray」，加起來的「絕對值最大」
# 這題我模仿 Vlad 的解法，找「最大」及「最小」的 sum，答案就持續更新
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        max_sum = min_sum = 0  # 對應「到 num 為止」的 max sum 及 min sum
        # 都不選的話，會是 0
        for now in nums:  # 現在要處理、當成「subarray」可能結束的那個數
            max_sum = max(0, max_sum + now)  # 不取用任何數 or 包含現在的數
            min_sum = min(0, min_sum + now)  # 不取用任何數 or 包含現在的數，可能會是負的哦
            ans = max(ans, max_sum, -min_sum)  # -min_sum 剛好是負數的絕對值
        return ans

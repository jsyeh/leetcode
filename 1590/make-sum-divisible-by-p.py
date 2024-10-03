# LeetCode 1590. Make Sum Divisible by P
# 題目給 nums 和 p，將 nums 刪掉某段「連續的subarray」，讓「其他加起來是p的倍數」
# 「倒過來想」，target 是 全部sum%p的值，如果「連續的subarray」sum%p的值==target，即可
# 如果，現在的 「running sum 減 target」在之前出現過，那這段加起來，剛好也是 target
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p  # 目標值（全部的數字加起來，是target），以下都在 % p 的世界
        if target==0: return 0  # 一開始就整除，答案直接是0，不用刪掉任何數
        recentI = {0:-1}  # 利用 recentI 存 running sum 最近出現的index座標
        runSum = 0
        ans = inf  # 想扣掉最小的距離，所以先放「無限大」，方便之後更新
        for i, num in enumerate(nums):
            runSum = (runSum + num) % p  # 新的 running sum
            prevTarget = (runSum - target + p) % p  # 之前希望的 target，+p是擔心有負數，但刪掉好像也可通過
            # 邊跑邊測，看 runSum最新 - target 之前「是否出現過」，也就是這段加起來，剛好也是 target
            if prevTarget in recentI:  # 出現的話，現在i-之前i,便是合理的subarray距離
                ans = min(ans, i-recentI[prevTarget]) # 距離若更小，就更新
            recentI[runSum] = i  # 更新 runSum 出現的位置，供下次使用
        if ans>=len(nums): return -1  # 如果 ans 都沒更新過，或是「全部刪除」都是不行
        return ans

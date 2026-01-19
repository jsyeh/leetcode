# LeetCode 746. Min Cost Climbing Stairs
# 爬樓梯「踩在第 i 個階梯」上，要付出 cost[i] 代價
# 一次可跨1格或2格，可從 0 或從 1 開始，問爬到最上一格，最少代價是多少？
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def helper(i):
            if i==0 or i==1: return 0
            return min(helper(i-1)+cost[i-1], helper(i-2)+cost[i-2])
        return helper(len(cost))

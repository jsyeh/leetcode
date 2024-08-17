# LeetCode 1014. Best Sightseeing Pair
# 每個景點的價值 values[i], 挑2個景點，讓 values[i]+values[j] + i - j 最大
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 通常會想到「2層迴圈」for i for j 來找
        # 其實可只用「1層迴圈」巡一輸，就找到答案
        ans = 0
        prevBest = values[0]  # 模仿 LeetCode 121 「低點買股票、高點賣股票」作法
        for i in range(1,len(values)):
            ans = max(ans, values[i] + prevBest - 1)
            prevBest = max(prevBest - 1, values[i])  # 更新「之前最佳值」
        return ans

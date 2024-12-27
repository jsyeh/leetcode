# LeetCode 1014. Best Sightseeing Pair
# 每個景點的價值 values[i], 挑2個景點，希望景點「價值高」，又希望兩個景點「距離近」，
# 目標是 values[i] + values[j] - (距離) 最大，即 values[i] +values[j] - abs(j-i) 最大
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 通常會想到「2層迴圈」for i 和 for j 來找
        # 其實可只用「1層迴圈」巡一輸，就找到答案
        ans = 0
        prevBest = values[0]  # 前面的（左邊）景點的最高價值（隨距離拉遠、慢慢「價值-1」）
        for j in range(1,len(values)):  # 右邊的景點（我刻意用j，以對應右邊）
            # 左邊（換算後）prevBest，右邊value[j]，距離1
            ans = max(ans, prevBest + values[j] - 1)  # 更新答案
            prevBest = max(prevBest - 1, values[j])  # 更新「左邊（換算後）最佳值」，舊值會隨時間「價值-1」
        return ans

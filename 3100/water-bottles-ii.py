# LeetCode 3100. Water Bottles II
# 原本可用 numExchange 個空瓶「換1瓶新飲料」，但 numExchange 每次 +1
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles  # 一開始的瓶子都能喝
        while numBottles >= numExchange:  # 瓶子數量 足夠再兌換一瓶
            ans += 1  # 一次只能兌換1瓶，拿來喝
            numBottles = numBottles - numExchange + 1  # 瓶子增減量
            numExchange += 1  # 每兌換一瓶後，標準提高 +1
        return ans  # 最後喝了幾瓶

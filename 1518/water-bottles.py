# LeetCode 1518. Water Bottles
# 空瓶子n個,可以換1瓶新的。請問最多可喝幾瓶水
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles # 一開始能喝這麼多瓶水
        while numBottles >= numExchange: # 喝完的空瓶，能再兌換
            exchange = numBottles // numExchange # 能兌換的數量
            ans += exchange # 又多喝了幾瓶
            numBottles = numBottles % numExchange + exchange # 剩的瓶+新增加的空瓶
        return ans

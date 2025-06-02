# LeetCode 135. Candy
# n 個小朋友「每人至少分1顆糖」，ratings[i] 比「左右鄰居」高的，就會更多顆
# 最少要幾顆糖「能完成分配的任務」
# 有人說「超不公平的」ex. 60,80,100,100,100,100 是分 1,2,3,1,1,1
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)  # 有 N 位小朋友
        candy = [1] * N  # 一開始，每人1顆糖
        for i in range(1,N):  # 左到右巡，如果「比左邊鄰居高」
            if ratings[i-1] < ratings[i] and candy[i] <= candy[i-1]:
                candy[i] = candy[i-1] + 1  # 就多1顆糖
        for i in range(N-2, -1, -1):  # 右到左巡，如果「比右邊鄰居高」
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1  # 就多1顆糖
        return sum(candy)

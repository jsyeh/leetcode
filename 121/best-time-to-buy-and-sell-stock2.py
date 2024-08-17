# LeetCode 121. Best Time to Buy and Sell Stock
# 最適合「買股票」、再「賣股票」的時間點，你最多能賺多少錢？
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        prevLowest = prices[0]  # 表示 prices[i]之前最低點

        ans = 0
        for i in range(1,N):  # 利用 DP 更新每天的「之前最低點」值
            prevLowest = min(prevLowest, prices[i])
            if prices[i] - prevLowest>ans:  # 可以賺更多是吧...
                ans = prices[i] - prevLowest # 去賺
        return ans


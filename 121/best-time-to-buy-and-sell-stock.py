class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        lowest = [0]*N # lowest[i] 表示 prices[i]之前最低點
        lowest[0] = prices[0]

        ans = 0
        for i in range(1,N):
            lowest[i] = min(lowest[i-1], prices[i])
            if prices[i]-lowest[i]>ans: # 可以賺更多是吧...
                ans = prices[i] - lowest[i] # 去賺
        return ans


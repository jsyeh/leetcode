class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 1: # 只有1天，根本來不及賣嘛
            return 0

        profit = [0]*N # profit[i] 在 day i 空手時，對應手上的現金量
        hold = [0]*N #hold[i] 在 day i 持有時，對應手上的現金量

        profit[0] = 0
        hold[0] = -prices[0]
        # 順序不能亂，要先把 day 0 填好，再處理下面的 day 1
        profit[1] = max(profit[0], hold[0]+prices[1])
        hold[1] = max(-prices[0], -prices[1]) #可能 day 0 or 1買的

        for i in range(2,N):
            profit[i] = max(profit[i-1], hold[i-1]+prices[i])
            hold[i] = max(hold[i-1], profit[i-2]-prices[i])
        
        # print(profit)
        # print(hold)
        return profit[N-1]



class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        hold = [0]*N # hold[i] 在第i天手上持有時，對應的Profit
        profit = [0]*N # profit[i] 在第i天手上空空時，對應的Profit
        
        hold[0] = - prices[0] # 買了，才算是「手上持有」
        profit[0] = 0 # 手上空空時的利潤

        for i in range(1,N):
            profit[i] = max(profit[i-1], hold[i-1]+prices[i]-fee)
            #           本來的值       vs. 持有在今天賣出得到現金
            hold[i] = max( hold[i-1], profit[i-1]-prices[i])
            #.           本來的值.   本來沒有，現在買進來
        print(profit)
        print(hold)
        return profit[N-1]



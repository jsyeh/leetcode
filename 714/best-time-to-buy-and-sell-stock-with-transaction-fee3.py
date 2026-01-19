# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
# prices[i] 是第i天的股價，每次交易要交易費 fee，問最多可賺多少錢？
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        @cache
        def helper(i, hasStack):
            if i==N: return 0
            if hasStack:  # 手上有股票：可不賣、可賣
                return max(helper(i+1,hasStack), prices[i]-fee+helper(i+1,False))
            else:  # 手上沒股票：可不買、可買
                return max(helper(i+1,hasStack), -prices[i]+helper(i,True))
        return helper(0,False)

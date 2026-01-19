# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
# prices[i] 是第i天的股價，每次交易要交易費 fee，問最多可賺多少錢？
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def helper(i, haveStack):  # 第i天, 手上有沒有股票
            if i==len(prices):  # 全部交易都結束
                if haveStack: return -inf  # 手上不能還有股票
                else: return 0  # 手上沒股票，很好，是交易的終止條件
            ans = helper(i+1, haveStack)  # 可能1: 今天不做交易
            # 可能2: 以下是有交易的狀況，一買、一賣，算「一次交易」 - fee
            if haveStack:  # 手上有股票，可以賣，得到 prices[i]
                ans = max(ans, helper(i+1, False) + prices[i])
            else:  # 手上沒股票，可以賣，花掉 prices[i] 再扣掉交易費
                ans = max(ans, helper(i+1, True) - prices[i] - fee)
            return ans
        return helper(0, False)  # 一開始，手上沒股票，答案最大是多少？

# LeetCode 3573. Best Time to Buy and Sell Stock V
# prices[i] 是股票每天的價格，最多可交易 k 次，交易時間不能重疊
# 可正常買賣（先買後賣）也可買空賣空（先賣、後補買），問最多賺多少錢
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @cache
        def helper(i, state, k):  # 處理第i天，交易剩k次，目前state：+1買、-1賣、0自由狀態
            if k<0: return -inf  # 不能是負的
            if i==len(prices):
                if state==0: return 0  # 順利完成
                else: return -inf  # 無法順利完成
            ans = helper(i+1, state, k)  # 不做變動（最基礎的行為，什麼都不動、發呆）
            if state<0:  # 手上欠股票，隨時可補買回
                ans = max(ans, helper(i+1, 0, k) - prices[i])  # 買回，沒欠股票，錢變少
            elif state>0:  # 有東西可以賣
                ans = max(ans, helper(i+1, 0, k) + prices[i])  # 賣掉，手上沒股票，錢變多
            else:  # state==0，目前沒有交易、自由狀態，隨時「可買」「可賣」
                ans = max(ans, helper(i+1, -1, k-1) + prices[i])  # 賣空，股票-1，得錢
                ans = max(ans, helper(i+1, +1, k-1) - prices[i])  # 買，股票+1，錢變少
            return ans
        ans = helper(0, 0, k)
        helper.cache_clear()
        return ans

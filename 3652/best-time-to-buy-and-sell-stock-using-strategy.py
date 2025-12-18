# LeetCode 3652. Best Time to Buy and Sell Stock using Strategy
# prices[i] 股價、strategy[i] 策略 -1買 0不動 1賣，（錢、股票無限）
# 最多可修改1次策略：連續k天「前半不動、後半賣」，想得到最多錢
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N = len(prices)  # 總天數 10^5 很大，不能暴力模擬。
        ans = original = sum( [prices[i]*strategy[i] for i in range(N)] ) 
        # 上面「原本策略」能得到的錢，下面用「長度k的毛毛蟲」測「是否更好」
        presum = sum( [prices[i]*strategy[i] for i in range(k)] )  # 原本前k項
        changed = sum( [prices[i] for i in range(k//2, k)])  # 「前半不動、後半賣」
        now = original - presum + changed  # 最左邊「毛毛蟲」
        ans = max(ans, now)  # 改前面k天的策略，更新答案
        for i in range(k, N):  # 逐一處理（「毛毛蟲」慢慢往右爬行）
            now += prices[i] * (1-strategy[i])  # 左邊的頭，吃一格「原本策略」變「賣」賺錢
            now -= prices[i-k//2]  # 中間「賣」變「不動」，「扣掉」賣的錢
            now += prices[i-k] * (strategy[i-k])  # 左邊尾巴，吐一格「不動」變「原本策略」
            ans = max(ans, now)  # 移動 k天的策略，更新答案
        return ans
        

# LeetCode 2110. Number of Smooth Descent Periods of a Stock
# 股票每日價錢 prices[i] 如果每日比前一日 -1 叫「平穩下降期」
# 可長可短, 最短「長度為1」也可以, 請問有幾段?
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1  # 你知道嗎? 長度為 1 (沒有前一天) 也是1種答案
        combo = 1  # 所以預設一定會有 1 次 combo
        # 找到 prices[i] 結尾時「最長」部分
        for i in range(1, len(prices)):
            if prices[i-1] - 1 == prices[i]:  # 持續符合
                combo += 1  # 持續加長
            else:
                combo = 1
            ans += combo  # 最長的長度有多長, 就有「幾組可能」
        return ans

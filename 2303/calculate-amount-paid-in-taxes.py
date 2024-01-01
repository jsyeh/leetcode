# 繳稅時，不同範圍用不同的稅率
# 計算繳稅總額時，收入就分段來扣稅
# 不過要小心 brackets[i][1] 稅率的單位是 percent, 要再除/100
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = min(brackets[0][0],income)*brackets[0][1]
        # 先用最低的稅率，算基本的稅有多少
        for i in range(len(brackets)): # 後面要增加的稅
            if income > brackets[i-1][0]: # 有超過前一級距
                ans += (min(brackets[i][0],income)-brackets[i-1][0]) * brackets[i][1]
        return ans/100 # 因稅率的單位是 percent 要再除100

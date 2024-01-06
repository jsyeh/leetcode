# 控制飲食dietPlan，計算你得幾分
# 連續k天加起來的 calories[i]+...+calories[i+k-1] 消耗的量 T
# T < lower 要扣1分
# T > upper 要加1分
# 評估最後會得幾分
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        total = 0
        for i in range(k): # 先加前k項
            total += calories[i]
        if total<lower: ans -= 1
        if total>upper: ans += 1
        # 接下來逐天統計（對應的）積分
        for i in range(len(calories)-k):
            total = total + calories[i+k] - calories[i]
            if total<lower: ans -= 1
            if total>upper: ans += 1
        return ans

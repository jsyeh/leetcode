# LeetCode 1176. Diet Plan Performance
# 控制飲食dietPlan，計算你得幾分
# 連續k天加起來的 calories[i]+...+calories[i+k-1] 消耗的量 T
# T < lower 要扣1分
# T > upper 要加1分
# 評估最後會得幾分
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        T = sum(calories[:k])
        if T < lower: ans -= 1
        if T > upper: ans += 1
        for i in range(len(calories)-k):
            T += calories[i+k]
            T -= calories[i]
            if T < lower: ans -= 1
            if T > upper: ans += 1
        return ans

# LeetCode 739. Daily Temperatures
# 每天 temperatures[i] 的值不同，想知道每天的「幾天後」會變熱
# ans[i] 就是「第i天」往右數，「幾天後」變熱。
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)  # 等待塞入答案（沒答案放0）
        stack = []  # 還在等待「塞入答案」
        for i,t in enumerate(temperatures):  # 左到右巡
            # 若有等待「塞入答案」的日子，且剛好「今天」比「那天」熱
            while stack and t > temperatures[ stack[-1] ]:
                i0 = stack.pop()  # 要填入的日子，是第i0天
                ans[i0] = i-i0  # 今天是第i天，要等待 (i-i0) 天
            # 處理完之前「等待處理」且可「剛好可處理」的日子，
            stack.append(i)  # 就把今天，放入「待處理」的 mono stack
        return ans

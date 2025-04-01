# LeetCode 2140. Solving Questions With Brainpower
# questions[i] 對應題目得分 points[i] 需耗腦力 brainpower[i]
# 解某題後，因耗腦力，之後連續 brainpower[i] 題都不能解
# 需依序解題，不想解可跳過，但跳過的題目，不能再回頭解它。最多能得幾分？
# 可用 Dynamic Programming 「函式呼叫函式」解這題
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        @cache
        def helper(i):  # 可決定要不要解第i題，目標是「得最高分」
            if i>=N: return 0  # 處理到最後面，後面沒題目了，終止條件 0 分
            points, brainpower = questions[i]  # 決定要不要解這題
            ans1 = points + helper(i+brainpower+1)  # 要解這題，就避開一些題
            ans2 = helper(i+1)  # 不解這題，「下面一位」
            return max(ans1, ans2)  # 哪個分數多，就用那個分數
        return helper(0)

# LeetCode 808. Soup Servings
# A B 兩種湯，有4種可能用法，機率各是 0.25：
# -100,-0 vs. -75,-25 vs. -50,-50 vs. -25,-75
# 兩種湯一開始的量是 n，A 先用完的機率是多少
# Dynamic Programming 「函式呼叫函式」看來可解，但 10^9 太大，怎麼辦？
class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def helper(a, b):  # 利用「函式呼叫函式」來解
            if a<=0 and b>0: return 1
            if a<=0 and b<=0: return 0.5
            if a>0 and b<=0: return 0
            p1 = helper(a-100, b) * 0.25  # 4種機率各 1/4
            p2 = helper(a-75, b-25) * 0.25
            p3 = helper(a-50, b-50) * 0.25
            p4 = helper(a-25, b-75) * 0.25
            return p1 + p2 + p3 + p4
        if n > 5000: return 1  # 重點：有人發現「湯的量夠大，A必勝」
        return helper(n, n)  # 「函式呼叫函式」

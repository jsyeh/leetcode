# LeetCode 50. Pow(x, n)
# 使用「函式呼叫函式」，將問題「每次減一半」，快速算出答案
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x
        if n==0: return 1

        now = self.myPow(x, n//2)
        if n%2==0: return now * now
        else: return now * now * x

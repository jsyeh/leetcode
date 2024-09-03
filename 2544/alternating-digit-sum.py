# LeetCode 2544. Alternating Digit Sum
# 每位數拆開、正、負交錯，加起來。
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = +1
        ans = 0
        for c in str(n):
            ans += sign * int(c)  # 依「正負」號「加起來
            sign *= -1  # 正、負交錯
        return ans

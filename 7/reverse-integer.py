# LeetCode 7. Reverse Integer
# 將 123 變 321
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1  # 先取出「正負號」
        x = x * sign  # 將 x 變成「正數」
        ans = 0
        while x>0:  # 利用「剝皮法」逐位取出來
            ans = ans * 10 + x % 10  # 再逐位組回去
            x = x // 10
        ans = sign * ans
        if ans < -2**31 or ans >= 2**31:
            return 0  # 題目強調「數字超過範圍」要 return 0
        return ans  # 將原本的「正負號」放回去

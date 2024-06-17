# LeetCode 633. Sum of Square Numbers
# 給 c 的值，問「到底有沒有a,b 使得 a*a+b*b==c」
# （好像有很多種作法）c 可能很大，不能用暴力法。 有人用binary search法，快
# 這裡只用「迴圈a」為主， b*b == c - a*a，開根號找b,看是否有整數（稍慢）
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a*a<=c:
            b = (c-a*a)**0.5  # 開根號
            # 下面看是否有整數的答案
            if b == int(b): return True
            a += 1
        # 都找不到答案的話，就失敗
        return False

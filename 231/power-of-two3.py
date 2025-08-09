# LeetCode 231. Power of Two
# 給你整數 n 請判斷它是不是 Power of Two (2的幾次方)
# 2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16 ...
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False  # 0 或 負數「失敗」
        binary = bin(n)[2:]  # 取「二進位」字串 0bxxxx 右邊數
        # 下面用吳邦一老師之前建議過的 字串.count('1') 有幾個'1' 
        if binary.count('1')==1: return True
        else: return False

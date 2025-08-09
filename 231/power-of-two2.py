# LeetCode 231. Power of Two
# 給你整數 n 請判斷它是不是 Power of Two (2的幾次方)
# 2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16 ...
# 就一直做除法，不是2的很多次方，就失敗。小心：0和負數「也失敗」
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False  # 0和負數「也失敗」
        while n>1:  # 因為 1 其實是成功的哦！比1大，才做除法
            if n%2 == 1: return False  # 剝皮法，有餘數就失敗
            n = n // 2  # 剝皮法，數字越來越小
        return True  # 都沒有失敗，就是成功!

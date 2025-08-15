# LeetCode 342. Power of Four
# 這題超簡單。可用「剝皮法」解決。
# 每次 %4 都要整除，剝到剩1就可結束True。無法整除，就False
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:  # 遇到負數 or 零，都失敗
            return False
        while n>1:  # 使用「剝皮法」
            if n%4 != 0: return False  # 無法整除，就失敗
            n //= 4  # 「剝皮法」
        return True  # 最後成功了

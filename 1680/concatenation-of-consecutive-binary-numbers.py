# LeetCode 1680. Concatenation of Consecutive Binary Numbers
# 將 1, 2, 3, ... n 的數，以二進位字串型式「全部接起來」再轉回整數
# 因 n <= 10^5 所以「全部接起來」數太大，要取 (10**9+7) 餘數
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9+7  # 數太大，要取餘數
        for i in range(1,n+1):  # 依序取出 1,2,3, ... n
            L = len(bin(i)) - 2  # 二進位 '0bXXX'長度，減'0b'長度
            # 「接起來」對應 (ans之前累積) * (2的長度次方) + (新的數)
            # ex. 1,2,3 就用 (1 * 4 + 2) * 4 + 3
            ans = (ans * (1<<L) + i) % MOD  # (1<<L)對應「2的L次方」
        return ans

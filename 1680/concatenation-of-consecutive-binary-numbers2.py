# LeetCode 1680. Concatenation of Consecutive Binary Numbers
# 將 1, 2, 3, ... n 的「二進位字串」全部接起來，再轉回整數
# 「接起來」對應 (ans之前累積) * (2的長度次方) + (新的數)
# 因 n <= 10^5 「全部接起來」數太大，要取 (10**9+7) 餘數
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9+7  # 數太大，要取餘數
        for i in range(1,n+1):  # 依序取出 1,2,3, ... n
            L = i.bit_length()  # 二進位的長度
            ans = ((ans << L) + i) % MOD  # << L 「乘上2的L次方」
        return ans

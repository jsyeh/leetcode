# LeetCode 868. Binary Gap
# 整數 n 以二進位表示，想找「兩個1之間」最大距離
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = zeros = 0
        for c in bin(n)[3:]:
            if c=='1':
                ans = max(ans, zeros+1)
                zeros = 0
            else: zeros += 1
        return ans

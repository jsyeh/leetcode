# LeetCode 1137. N-th Tribonacci Number
# Fibonacci 改名 Tribonacci 
# 就照著實作即可
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0,1,1]
        for i in range(3, n+1):
            a.append(a[-1]+a[-2]+a[-3])
        return a[n]

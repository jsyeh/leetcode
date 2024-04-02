# Fibonacci 改名 Tribonacci 
# 就照著實作即可
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1] # 前3項
        if n<3: return a[n]
        for i in range(3,n+1): # 後面逐項更新
            a.append(a[i-1] + a[i-2] + a[i-3])
        return a[-1] # 最後1項
# case 38/39: n:0

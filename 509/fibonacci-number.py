class Solution:
    def fib(self, n: int) -> int:
        f = [0]*(31)
        f[0] = 0
        f[1] = 1 # 如果n是0，就會出錯，所以陣列可宣告大一點
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

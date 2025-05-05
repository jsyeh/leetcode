# LeetCode 790. Domino and Tromino Tiling
# 有兩種形狀的骨牌，傳統 1x2 及 L型 的骨牌，問 2xn 有幾種可能排法
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def helper(n):
            if n==0: return 1
            if n==1: return 1
            if n==2: return 2
            # 第1個，可以直放，可以橫放
            ans = helper(n-1) + helper(n-2)
            # 也可以用 L型的方法放（有兩種L型），會對應「收尾的L型」
            for i in range(3, n+1, 2):  # 「收尾的L型」收在哪裡
                ans = (ans + helper(n-i) * 2) % MOD  # 有兩種L型
            # 也可以用「兩個L長邊對接」的形式
            for i in range(4, n+1, 2):
                ans = (ans + helper(n-i) * 2) % MOD
            return ans % MOD
        return helper(n)

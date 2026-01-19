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
            if n==3: return 5
            ans = helper(n-1)  # 新的1層「直放」
            ans += helper(n-2)  # 新的2層「橫放」
            # 新的一堆L型
            for i in range(3,n+1):
                ans = (ans + helper(n-i) * 2) % MOD
            return ans
        return helper(n)

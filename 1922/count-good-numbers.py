# LeetCode 1922. Count Good Numbers
# n 位數中，符合「左邊」數起來「偶數位放偶數、奇數位放質數」有幾個？
# 可利用「函式呼叫函式」有效率找出「偶數位5種可能、奇數位4種可能」的總數
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7  # 因最多 10^15 約 1000兆位數很大，所以要取「MOD餘數」
        @cache  # 利用「函式呼叫函式」每次「切一半」再乘起來，配合 cache 變快
        def helper(n, start):  # n位數時，開始位數 start 會對應 4+start 種可能
            if n==0: return 1  # 終止條件：切到變0位數，要乘上所有數
            if n==1: return 4+start  # 偶數，會回傳5、奇數，會回傳4
            n2 = n//2  # 「切一半」的位數
            ans = helper(n2, start)  # 函式呼叫函式，「左半」的開始，與原本開始
            if n%2==1: ans = ans * (4+start) % MOD  # 最後剩下的位數，對應 4 or 5

            if n2%2==0: ans = ans * helper(n2, start) % MOD  # 函式叫函式
            else: ans = ans * helper(n2, 1-start) % MOD  # 函式呼叫函式
            return ans
        return helper(n, True)  # start 時，True 對應 4+1、False對應 4+0

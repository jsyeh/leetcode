# 找出「共同的因數」有幾個，其實等價於「最大公因數」的因數有幾個
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(a,b)->int:
            if b==0: return a
            return gcd(b, a%b)
        
        g = gcd(a,b)
        ans = 0
        for i in range(1,g+1):
            if g%i==0: ans += 1 # 有幾個「能整除」的因數
        return ans

# 簡化的分數，分母必須<=n
# 小心，不能有 2/4 因為它會「約分」成 1/2
# 所以可以暴力產生「分數」的字串，但避開「能約分」即gcd>1的數
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b)->int: # 找最大公因數
            if b==0: return a
            return gcd(b, a%b)
        # numerator分子 denominator分母 但我用 upper lower 好了
        ans = []
        for lower in range(2,n+1):
            for upper in range(1,lower):
                if gcd(lower,upper)==1: # 最大公因數=1 不可約分
                    ans.append(str(upper)+'/'+str(lower))
        return ans

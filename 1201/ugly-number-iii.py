# 因為 n<=10^9太大，無法使用篩子法
# 但可以過來，猜 ans 後，看 ans 是第幾個 ugly number
# +a倍 +b倍 +c倍 -ab倍 -bc倍 -ac倍 +abc倍
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b) -> int:
            if a==0: return b
            if b==0: return a
            return gcd(b, a%b)

        def lcm(a, b) -> int:
            return a*b//gcd(a,b)

        def uglyID(guess:int) -> int:
            ans = guess//a + guess//b + guess//c
            ans -= guess//lcm(a,b) + guess//lcm(a,c) + guess//lcm(b,c)
            ans += guess//lcm(a,lcm(b,c))
            return ans
        
        left, right = 0, 10**10
        while left<right:
            mid = (left+right)//2
            if uglyID(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left

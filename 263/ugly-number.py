# 只能被2,3,5 整除的數
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0: return False # 因要正整數
        while n%2==0:
            n //= 2
        while n%3==0:
            n //= 3
        while n%5==0:
            n //= 5
        return n==1

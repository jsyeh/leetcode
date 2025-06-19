# LeetCode 1952. Three Divisors
# n 是不是剛好有 3 個因數
class Solution:
    def isThree(self, n: int) -> bool:
        divisor = 0  # 有幾個「可整除」的因數
        for i in range(1,n+1):
            if n%i==0: divisor += 1
        return divisor == 3  # 是不是「剛好3個」？

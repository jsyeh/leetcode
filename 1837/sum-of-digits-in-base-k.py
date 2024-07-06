# LeetCode 1837. Sum of Digits in Base K
# 想把10進位數字n，改成k進位的數字後，把每1位數都加起來
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n>0:  # 用簡單的剝皮法，就可以算出來了
            ans += n % k
            n = n // k
        return ans

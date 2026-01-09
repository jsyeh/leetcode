# LeetCode 1071. Greatest Common Divisor of Strings
# 找到字串的 gcd 最大公因數
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)
        g = gcd(N1, N2)
        if str1[:g] != str2[:g]: return ''
        if str1 == str1[:g]*(N1//g) and str2 == str1[:g]*(N2//g):
            return str1[:g]
        else: return ''

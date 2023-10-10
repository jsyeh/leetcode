# 字串的GCD：相同的子字串，想到可以用字串減法
# 但是看了 Editorial 的解答後，發現它的解法更簡單：
# 字串「前」「後」接起來，必須相同，才代表有GCD的子字串
# 確認有GCD子字串時，依其gcd()長度的值，就直接是答案
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 字串「前」「後」接起來，必須相同，才代表有GCD的子字串
        if str1+str2 != str2+str1:
            return ""  # 不相同的話，就是空字串
        
        # Python 竟然有 gcd()可以用
        N = gcd(len(str1), len(str2))
        return str1[:N]
        

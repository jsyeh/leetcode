# 字母都相同的substring子字串, 總共出現幾次
# 看起來是典型的 DP 題目。
# a bb ccc aa
# 1
#   1    b出現1次
#   21   b出現2次, bb出現1次
#      1    c出現1次
#      21   c出現2次, cc出現1次
#      321  c出現3次, cc出現2次, ccc出現1次
#          1   a出現1次
#          21  a出現2次, aa出現1次
# 1 21 321 21 共13次
# 1 12 123 12 可以倒過來看
class Solution:
    def countHomogenous(self, s: str) -> int:
        N = len(s)
        ans = 1 # s[0]沒有前一項, 所以直接先設1次, 迴圈要避開它
        combo = 1 # 1個獨立的
        for i in range(1,N): # 避開 s[0] 的迴圈
            if s[i] == s[i-1]: # 與前項相同
                combo += 1 # 又多了一個相同
                ans += combo # 倒過來加
            else: # 與前項不同
                combo = 1 # 回到1個獨立的
                ans += combo # 倒過來加
            ans = ans % 1000000007
        return ans

# LeetCode 8. String to Integer (atoi)
# 把字串「變成 int」需於 -2**31 ... (2**31-1) 範圍內
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # 先裁掉左右的空白
        if len(s)==0: return 0
        if s[0]=='-' or s[0]=='+' or s[0].isdigit(): s2 = s[0]
        else: return 0
        for c in s[1:]:
            if c.isdigit(): s2 += c
            else: break
        if len(s2)==1 and (s2[0]=='-' or s2[0]=='+'): return 0
        ans = int(s2)
        if ans < -2**31: return -2**31
        if ans > 2**31-1: return 2**31-1
        return ans

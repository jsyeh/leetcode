# LeetCode 65. Valid Number
# 字串 s 是不是「合理的數字」
# 規則：decimal number 或 integer，都合理
# 字母e的後面有整數
# 
class Solution:
    def isNumber(self, s: str) -> bool:
        counter = Counter(s)
        for c in counter:
            if c not in "+-0123456789.eE": return False
        #if s=="inf" or s=="-inf" or s=="+inf" or s=="Infinity": return False
        try:
            ans = float(s)
            return True
        except:
            return False

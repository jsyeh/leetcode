# LeetCode 394. Decode String
# 將字串解碼
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nowN, nowS = 0, ''
        for c in s:
            if c.isdigit():  # 如果是數字
                nowN = nowN * 10 + int(c)
            elif c.isalpha():  # 如果是字母
                nowS += c
            elif c=='[':  # 上括號：數字、字串放入stack
                stack.append( (nowN, nowS) )
                nowS, nowN = '', 0
            elif c==']':  # 下括號：取出數字、字串
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS
        return nowS

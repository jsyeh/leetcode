# LeetCode 394. Decode String
# 將字串解碼
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        now = 0
        nowStr = ""
        for c in s:
            if c=='[':
                stack.append(nowStr)
                stack.append(now)
                nowStr = ""
                now = 0
            elif c==']':
                num = stack.pop()
                prevStr = stack.pop()
                nowStr = prevStr + num * nowStr
            elif c.isdigit():
                now = now * 10 + int(c)
            else:
                nowStr += c
        return nowStr

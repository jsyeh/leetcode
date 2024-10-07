# LeetCode 2696. Minimum String Length After Removing Substrings
# 可把 "AB" 或 "CD" 刪除，問字串s最後可變多短？
class Solution:
    def minLength(self, s: str) -> int:
        stack = []  # 其實使用 stack 就可「持續」看能否刪除了
        for c in s:
            stack.append(c)
            if len(stack)>=2:  # 長度夠，便可檢測「能否刪除」
                if stack[-2]=='A' and stack[-1]=='B':
                    stack.pop()  # 配對成功，便能刪除
                    stack.pop()
                elif (stack[-2]=='C' and stack[-1]=='D'):
                    stack.pop()  # 配對成功，便能刪除
                    stack.pop()
        return len(stack)

# LeetCode 2390. Removing Stars From a String
# 字串裡，每次讀到 '*' 就要「再刪掉前1個字母」，可用 stack 完成
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c=='*': stack.pop()
            else: stack.append(c)
        return ''.join(stack)

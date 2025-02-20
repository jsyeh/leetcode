# LeetCode 2309. Greatest English Letter in Upper and Lower Case
# 「同時有大寫、小寫」的字母，找到最大的。
class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if c in s and c.lower() in s:
                ans = c
        return ans

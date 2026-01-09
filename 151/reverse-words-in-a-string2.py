# LeetCode 151. Reverse Words in a String
# 將 words 裡的 word 倒過來放
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join( reversed(s.split()) )

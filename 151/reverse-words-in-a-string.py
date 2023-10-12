class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()
        return " ".join(reversed(ans))

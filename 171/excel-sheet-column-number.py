# 把字母拆開來，再用26進位來解決
# 最後記得轉成 1-index
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ans * 26 + ord(c)-ord('A') + 1
        return ans

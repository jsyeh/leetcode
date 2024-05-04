# 每一步，可移除一小段 Palindrome 迴文 subsequence
# 問要「幾步」才能將字串 s 刪光光？
# 因為 s 裡只有 'a' 或 'b' 所以超簡單。
# 但其實更簡單，因為 subsequence 可以跳著選。
# 「最差」也只要刪「2步」：先刪全部的'a'(一定是迴圈)，再刪剩下的'b'
# 所以如果「已經是迴圈」就return 1 不然就 return 2
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[-1::-1]:
            return 1
        return 2


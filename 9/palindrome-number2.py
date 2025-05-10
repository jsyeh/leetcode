# LeetCode 9. Palindrome Number
# 判斷 x 是不是「迴文」
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False  # 負數一定不是
        # 另一種寫法，利用 Python 轉成字串、反過來，就可以了
        if x == int(''.join(reversed(str(x)))): return True
        return False

# LeetCode 9. Palindrome Number
# 判斷 x 是不是「迴文」
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0  # 放「倒過來」的數
        n = x  # 備份一下原本的數字
        while n > 0:  # 利用「剝皮法」
            ans = ans * 10 + n % 10
            n = n // 10
        if x == ans: return True  # 若原本數==倒過來的數，就是「迴文」
        return False

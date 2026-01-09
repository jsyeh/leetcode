# LeetCode 345. Reverse Vowels of a String
# 將「母音」的順序「反過來」
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for c in s:  # 第一次，先巡一次，挑出全部的母音
            if c in 'aeiouAEIOU': vowels.append(c)
        ans = []
        for c in s:  # 第二次，將母音（倒過來）pop()回去
            if c in 'aeiouAEIOU': ans.append(vowels.pop())
            else: ans.append(c)
        return ''.join(ans)

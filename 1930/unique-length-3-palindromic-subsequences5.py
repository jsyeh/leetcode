# LeetCode 1930. Unique Length-3 Palindromic Subsequences
# s 字串裡，可湊出「幾種」3個字母的迴文？ ex. aabca 會有 aaa, aba, aca 三種
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 看了 Code Sample 裡，有超精簡的程式，決定也試試看
        ans = 0  
        for c in set(s):  # 針對所有「曾出現過的字母」
            start, end = s.find(c), s.rfind(c)  # 起點、終點
            ans += len(set(s[start+1:end]))  # 中間有幾種字母
        return ans

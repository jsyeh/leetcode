# LeetCode 1930. Unique Length-3 Palindromic Subsequences
# 在字串 s 可跳著挑 3個字母，有幾種可能的 palindrome 迴文。
# 3個字母只要「頭尾相同」，即是「迴文」。先記錄字串中「每種字母」頭尾位置即可。
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}  # first['a'] 代表 'a' 第1次出現的位置
        last = {}  # last['a'] 代表 'a' 最後1次出現的位置
        for i, c in enumerate(s):  # 字串的迴圈
            if c not in first:  # 如果之前沒出現過
                first[c] = i  # 就記下第1次出現的位置
            last[c] = i  # 持續更新，便知此字母最後一次出現的位置
        # 經以上迴圈，便確定每個字母第1次、最後1次出現位置
        ans = 0
        for c in first:  # 在 first 出現過的字母 c
            middle = set()  # 中間有哪些字母呢？
            for i in range(first[c]+1, last[c]):
                middle.add(s[i])  # 中間的字母，加入 middle 集合
            ans += len(middle)  # 中間有幾種字母，那迴文數就增加「這麼多」
        return ans  # 便能知有多少「3個字母」且「同尾相同」的答案

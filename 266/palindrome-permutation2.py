# LeetCode 266. Palindrome Permutation
# 若想組合 Palindrome迴文，每個字母都要偶數，最多只能1個奇數
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)  # 使用 Counter 數字母出現次數
        print(counter)
        odd = 0
        for c in counter:  # 針對每一種出現的字母 c
            if counter[c]%2==1:  # 若出現奇數次
                odd += 1  # 就記起來
        return odd <= 1  # 能容忍「最多1個奇數」


# LeetCode 1657. Determine if Two Strings Are Close
# 它的操作，是任意交換位置，還可以任意字母對調翻轉。所以統計好數量，並看字母set相同，就成功
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1)==set(word2)

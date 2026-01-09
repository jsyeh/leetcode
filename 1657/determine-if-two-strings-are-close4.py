# LeetCode 1657. Determine if Two Strings Are Close
# 它的操作，是任意交換位置，還可以任意字母對調翻轉。所以統計好數量，並看字母set相同，就成功
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        return set(counter1.keys()) == set(counter2.keys()) and sorted(counter1.values()) == sorted(counter2.values())

# LeetCode 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
# 找一下 searchWord 是否在 sentence 裡有出現在字首
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # 先把 sentence 斷成很多 words
        L = len(searchWord) # 待查的 searchWord 的長度 L
        for i in range(len(words)):  # 針對 words 裡，每個 words[i] 逐一比對
            # 取出 words[i] 的前 L 個字母，看與 searchWord 是否相同
            if searchWord == words[i][:L]:
                return i+1  # 題目是 1-index 從1開始，所以要 +1
        return -1

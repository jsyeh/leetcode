# 把 sentence 斷句成一堆 words, 看 裡面有沒有字的前面prefix 是 searchWord
# 使用 w[:lenS] 與 searchWord 做比較即可
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split() # 斷字
        lenS = len(searchWord)
        for i, w in enumerate(words):
            if len(w)<lenS: continue # 要小心長度不夠的問題
            if w[:lenS] == searchWord: # 字串前面 lenS 個字母相同
                return i+1 # 因為是 1-indexed 所以要 +1
        return -1

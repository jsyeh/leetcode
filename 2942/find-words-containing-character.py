# 想知道 x 在 words 裡出現的狀況
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i,word in enumerate(words): # 錯對每個 word
            if x in word: ans.append(i) # 如果x有在 word 裡出現，答案+1個
        return ans

# words 裡，找出第1個符合的 palindrome 迴文。找不到就 return ""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words: # 逐字檢查每個word
            bad = False
            N = len(word)
            # 下面的迴文檢查，Python跑得慢。有人用 if word == word[::-1] 會較快
            for i in range(N//2): # 逐字母檢查
                if word[i] != word[N-1-i]: # 頭尾不同
                    bad = True # 就失敗
                    break # 可提早結束這輪檢查
            if not bad: return word # 若沒有壞，就找到了
        return "" # 前面都沒找到，就是「找不到」

# 檢查 words[i] 裡, 有幾個是 s 的 prefix
# 就把 s 變成 s[:word長度] 即可用 if 來比較
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        lenS = len(s)
        for word in words:
            N = len(word)
            if N>lenS: # 太長的話, 一定不可能
                continue
            if s[:N] == word: 
                ans += 1
        return ans

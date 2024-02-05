# 只能在 在某一個字串裡出現的 subsequence，問它最長的長度
# 一開始沒什麼頭緒。但看了 Dicussions裡，很多人覺得這題很糟。
# 再偷看答案後，能夠體諒大家的感覺。答案跟題目沒什麼關係。
# 就一個很巧合的規則，讓程式變得極為簡單。
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b: return -1
        else: return max(len(a),len(b))

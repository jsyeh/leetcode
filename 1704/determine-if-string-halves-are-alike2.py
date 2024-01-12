# 1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s) # 字串的長度 ex. s="textbook"
        mother = "aeiouAEIOU"
        count = 0
        for i in range(N):
            if i<N//2 and s[i] in mother: count += 1 #左半邊 且是母音
            if i>=N//2 and s[i] in mother: count -= 1 #右半邊
        return count==0

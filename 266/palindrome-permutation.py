# 若想組合 Palindrome迴文，每個字母都要偶數，最多只能1個奇數
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = defaultdict(int) # 用字典來統計，值預設整數0
        for c in s: # 每個字母
            d[c] += 1 # 對應的次數+1
        odd = 0 # 有幾個字母出現奇數?
        for c in d: # 針對字典裡每個字母的出現次數分析
            if d[c]%2==1: odd += 1 # 這個字母出現次數「奇數」
        if odd<=1: return True # 不超過1個奇數，可！
        else: return False

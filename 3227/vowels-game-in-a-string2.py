# LeetCode 3227. Vowels Game in a String
# 兩人依序將字串 s 裡刪掉一些 substring
# Alice 要刪「含奇數個母音」的substring、Bob 要刪「含偶數個母音」的substring
# 兩人都盡力玩，最後 Alice 會得勝嗎？ 這題其實「子音」完全不重要。數一數「有幾個母音」即可
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelSet = set('aeiou')  # 可快速找「母音」
        for c in s:
            if c in vowelSet: return True  # 只要有「母音」Alice 必勝
        return False  # Alice 沒有得勝，就輸了

# 希望字是「全大寫」、「全小寫」、「首字大寫」的任一種 True
# 其他都 False
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower(): return True
        if word == word.upper(): return True
        if word == word.capitalize(): return True
        return False

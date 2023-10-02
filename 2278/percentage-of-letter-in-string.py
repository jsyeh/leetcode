# 就數數，便能知道百分比
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        table = {}
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        
        if letter not in table:
            return 0 # 不存在的字母，答案是0
            
        return table[letter]*100//len(s)

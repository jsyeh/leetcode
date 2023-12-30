# 迴文判斷時，能容忍「有一個」或「有兩個」字母換掉
class Solution:
    def makePalindrome(self, s: str) -> bool:
        N = len(s)
        bad = 0
        for i in range(N//2): # 迴圈只要比到一半就可以了
            if s[i]!=s[N-1-i]: bad += 1 # 增加1個壞掉
        if bad<=2: return True # 如果壞掉的數量有限，就成功
        else: return False
# case 62/83: "zbcfedcba" 抽換2個字母，也可以

# 把s裡「每個數值」的字母，變成「對應的字母」
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s) # 先變成 list，才能在迴圈裡修改
        for i in range(1, len(s), 2): # 每個對應的數字
            s[i] = ord(s[i-1])+int(s[i]) # 前一項的ascii值，加上位移
            s[i] = chr(s[i]) # 再轉回字母
        return ''.join(s)


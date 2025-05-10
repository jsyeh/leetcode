# LeetCode 12. Integer to Roman
# 把數字，變成「羅馬大寫數字」
class Solution:
    def intToRoman(self, num: int) -> str:
        table = { 1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
        ans = ''
        for i in table:
            while num >= i:  # 先做除法
                ans += table[i]
                num -= i
            # 剩下的數，看有無機會，變成「倒數」的 9 或 4 系列
            if num*10>i and str(i)[:1]=='1' and str(num)[:1]=='9':
                ans += table[i//10] + table[i]
                num -= i//10 * 9
            elif num*10>i and str(i)[:1]=='1' and str(num)[:1]=='4':
                ans += table[i//10] + table[i//10*5]
                num -= i//10 * 4
        return ans

# LeetCode 258. Add Digits
# 利用「剝皮法」將每個位數「加起來」，再利用 while 迴圈，重覆做到<=0
class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while ans>9:  # 外面的 while 迴圈，看答案是否太大
            num = ans  # 準備進行「剝皮法」，記得「變數要更新一下」
            ans = 0  # 新的答案，累積「每個位數的值」
            while num>0:  # 簡單的「剝皮法」迴圈
                ans += num % 10
                num //= 10
        return ans

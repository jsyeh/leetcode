# LeetCode 2180. Count Integers With Even Digit Sum
# <=num 的數字中，有幾個「每位數加總」是「偶數」？就暴力測測即可
class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(2,num+1):  # 測「範圍」內全部的數字
            total = 0
            for c in str(i):  # 先變成字串，再逐個字母加總
                total += int(c)
            if total%2==0: ans += 1  # 最後是「偶數」，答案+1
        return ans

# LeetCode 2894. Divisible and Non-divisible Sums Difference
# 1...n 這些數，逐一檢查是不是 m 的倍數、能不能被 m 整除
# 不能整除的放 num1，能整除的放 num2，最後 return num1-num2
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0  # 開始統計
        for i in range(1, n+1):  # 逐一分析
            if i%m!=0:  # 不可整除
                num1 += i  # 放在 num1
            else:  # 可以整除
                num2 += i  # 放在 num2
        return num1 - num2  # 最後相減

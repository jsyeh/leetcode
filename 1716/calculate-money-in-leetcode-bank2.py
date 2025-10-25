# LeetCode 1716. Calculate Money in Leetcode Bank
# 每天存錢：一開始，週一存1元、週二存2元...週日存7天
# 下週一存2天、下週二存3元...下週日存8元。請問n天後，會存多少錢？
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0  # 因為 n 很小，只要用 for 迴圈慢慢模擬即可
        today = 1  # 第1天存
        for i in range(1, n+1):  # 週1是1，週日是7的倍數
            ans += today  # 今天存 today 元
            today += 1  # 隔天要比前一天「多1元」
            if i%7==0: today -= 6  # 週日要扣回來
        return ans

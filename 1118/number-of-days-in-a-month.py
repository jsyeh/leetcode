# 某年某月有幾天，只要注意閏年即可
class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        ans = [31,28,31,30,31,30,31, 31,30,31,30,31] # 0-index
        if year%400==0 or (year%100!=0 and year%4==0):
            ans[1] += 1 # 2月有29天
        return ans[month-1] # 0-index

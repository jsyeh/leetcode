# year 介於 1971-2100 之間
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        day = [0, 31,28,31,30,31,30,31, 31,30,31,30,31] # 每個月有幾天
        def days(s:str)->int: # 換算出從 1971年開始到現在的天數
            yy, mm, dd = list(map(int, s.split('-') ))
            # 要解決閏年的問題
            ans = dd # 先加日
            for y in range(1971, yy): # 先算年, 之前有幾年、多少閏年
                if y%400==0 or (y%100!=0 and y%4==0): ans += 366
                else: ans += 365
            now_leap = yy%400==0 or (yy%100!=0 and yy%4==0)
            for m in range(1, int(mm)): # 再算月
                ans += day[m]
                if m==2 and now_leap: ans += 1
            return ans
        return abs( days(date1) - days(date2) )

# case 70/105: "2009-08-18" "2080-08-08" 答案是 25923 但我少了1天
# 原來是 2080年是閏年, 但我沒有考慮到當年度的狀況

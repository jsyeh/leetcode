# 要先解決 leap year 的部分
class Solution:
    def dayOfYear(self, date: str) -> int:
        yy,mm,dd = list(map(int, date.split('-') ))
        print(yy,mm,dd)
        days = [0,31,28,31,30,31,30,31, 31,30,31,30,31]
        ans = dd # 先解決「日」
        for i in range(mm): # 再依照「月」
            ans += days[i] # 加入「每月」對應的天數

        if mm<=2: return ans # 不用管2月之前的潤年部分

        # 下面是潤年的計算
        leap = 1 if yy%400==0 or (yy%100!=0 and yy%4==0) else 0
        return ans + leap # 3月之後都要考慮平年/潤年的2月天數

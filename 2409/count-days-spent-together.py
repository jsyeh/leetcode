# 日期的格式 mm-dd 要換算成「一年的第幾天」其中2月有28天
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convertDays(s):
            mm, dd = s.split('-')
            ans = int(dd)
            for i in range(int(mm)-1):
                ans += days[i]
            return ans

        arriveAlice = convertDays(arriveAlice)
        leaveAlice = convertDays(leaveAlice)
        arriveBob = convertDays(arriveBob)
        leaveBob = convertDays(leaveBob)

        '''
        # 算出對應「第幾天」的日子後, 利用 for 迴圈, 每天檢查「兩個人是否都在那一天出現」
        # 算是很笨的暴力法, 不過就不用太思考各種可能了。
        ans = 0
        for d in range(370):
            if arriveAlice <= d <= leaveAlice and arriveBob <= d <= leaveBob:
                ans += 1
        '''
        # 比較好的解法, 則是用 「兩人最早離開的時間」 - 「兩人最晚到時間」 + 1天(頭尾相同也要算1天)。
        # 同時如果是負的話, 就是 0 天
        ans = min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1
        ans = max(0, ans)
        return ans

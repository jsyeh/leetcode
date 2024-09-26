# LeetCode 729. My Calendar I
# 行事曆裡「預約時間」若時間有衝突，要false。沒衝突就True預約那段時間
# 最多呼叫 book() 1000次，數字不會太大，所以暴力法就可通過。
class MyCalendar:

    def __init__(self):
        self.booked = []  # 預約的時段都放在這裡

    def book(self, start: int, end: int) -> bool:
        # 超沒效率的暴力法, 全部都去試, 哈哈!
        for s,e in self.booked:  # 針對現有預約的時段,逐一檢查
            # 不重疊的原則: 一個先結束、另一個才開始, 即 e<=start 或 end<=s
            if not (e<=start or end<=s): # 兩種時間不會重疊的規則「無法通過」
                return False
        # 若能通過, 記下時間
        self.booked.append((start,end))  # 更新「預約的時段」
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

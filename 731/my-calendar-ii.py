# LeetCode 731. My Calendar II
# 行事曆裡「預約時間」，這次題目變得比較難：可衝突2次，但不能衝突第3個。
# 題目 Hint 建議「兩個sorted list」來存「1次」及「2次」的時段。但我不太會用 sorted list。
# 我在 Solutios 看到 awice 分享的「暴力法」，粗暴簡單，就試寫看看，竟然成功、沒超時，太好了!
class MyCalendarTwo:

    def __init__(self):
        self.booked1 = []  # 有預約1次的時段
        self.booked2 = []  # 有預約2次的時段

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booked2:  # 還是用暴力法試，如果有壓到「預約2次」，就失敗
            if not (e <= start or end <= s):  # 兩個沒有重疊的狀況，都不成立，就不行
                return False  # 失敗、無法插入此次預約
        # 沒有失敗，就是成功。需要更新 booked1 和 booked2
        for s, e in self.booked1:  # 還是暴力法，看 booked1 會不會重疊、升級到 booked2
            if not (e <= start or end <= s):  # 沒有「沒重疊」（就是有重疊），要升級
                self.booked2.append((max(start,s), min(end,e)))  # 重疊：(開始的右邊, 結束的左邊)
        self.booked1.append((start,end))
        return True  # 成功預約



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

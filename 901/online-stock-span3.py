# LeetCode 901. Online Stock Span
# 某天的股票，是「連續n天的最高點」，找出每天的n
# 實作 class StockSpanner 裡的 next(price) 函式，一邊記錄、一邊找出「天數」
class StockSpanner:
    def __init__(self):
        self.stack = [inf]  # 放價錢 mono stack 要往下掉
        self.stackI = [-1]  # 放對應的第i天
        self.I = 0
    def next(self, price: int) -> int:  # 今天 price 是「最近幾天」的最高？
        while self.stack[-1] <= price:
            self.stack.pop()
            self.stackI.pop()
        ans = self.I - self.stackI[-1]
        self.stackI.append(self.I)
        self.stack.append(price)
        self.I += 1
        return ans

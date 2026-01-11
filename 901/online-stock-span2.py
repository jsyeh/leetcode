# LeetCode 901. Online Stock Span
# 某天的股票，是「連續n天的最高點」，找出每天的n
# 實作 class StockSpanner 裡的 next(price) 函式，一邊記錄、一邊找出「天數」
class StockSpanner:
    def __init__(self):
        self.day = 0  # 從第0天開始計算，現在是第幾天？
        self.stack = []  # 實作 mono  stack 

    def next(self, price: int) -> int:
        self.day += 1  # 又過了1天
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()  # 如果股價比 mono stack 高，繼續吐

        if self.stack:  # 如果還有 mono stack 找得到「更高的點」
            ans = self.day - self.stack[-1][1]  # 答案是兩天相減
        else:  # 如果 mono stack 清空
            ans = self.day  # 答案是天數減0
        self.stack.append((price,self.day))  # 今天的股價壓入 stack
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

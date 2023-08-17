# 想知道某天的股價，可以罩住「往前幾天」的股價，也就是「管」幾天的股價
class StockSpanner:
    
    def __init__(self):
        self.stack = deque()
        self.stack.append([999999, 0]) # 第0天之牆，沒人能蓋掉它
        self.day = 0
        # 在 class StockSpanner 裡有個變數是 self.stack 可供 next()使用
        # 裡面要存 [price, day]

    def next(self, price: int) -> int:
        # 一邊呼叫 next(今日股價) 一邊 return 「它可往前管幾天」
        self.day += 1
        while len(self.stack)>0 and self.stack[-1][0] <= price:
            self.stack.pop() # 如果 stack[最後一筆]不夠蓋住price,就丟掉
        ans = self.day - self.stack[-1][1] # ans = 日期差
        self.stack.append([price,self.day]) # 塞今天的股價資訊
        return ans
# case 2/99: ["StockSpanner","next","next","next","next","next"]
# [[],[31],[41],[48],[59],[79]]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

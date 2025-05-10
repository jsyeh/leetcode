# LeetCode 359. Logger Rate Limiter
# 設計 Logger 會在 shouldPrintMessage() 時，決定「要不要印」
# 前一次 t 時間印，之後 t+10 之後才能再印
class Logger:

    def __init__(self):
        self.prev = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.prev and timestamp < self.prev[message] + 10:
            return False  # 在最近10秒內有印過，不要印

        self.prev[message] = timestamp  # 可以印，記下時間
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

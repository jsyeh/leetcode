# moving average 就是邊加邊平均
# 最多收 size 個數來算平均，但要把舊的丟掉
# 想到可以用 deque() 來節省空間/循還利用
class MovingAverage:

    def __init__(self, size: int):
        self.size = size # 記下來
        self.sum = 0 # 一開始沒有值
        self.queue = deque(maxlen = size) # 省空間

    def next(self, val: int) -> float:
        self.sum += val # 新的值加到 sum 裡
        if len(self.queue) >= self.size:
            self.sum -= self.queue.popleft()
            # 如果爆表，那要丟掉最舊的那個
        self.queue.append(val) # 新的值加入 queue
        return self.sum / len(self.queue) # 新的平均


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

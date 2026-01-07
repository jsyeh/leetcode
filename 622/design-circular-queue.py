# LeetCode 622. Design Circular Queue
# 實作 enQueue() deQueue() Front() Rear() isEmpty() isFull()
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * k
        self.head = 0
        self.tail = -1  # 尾巴的移動有點特別
        self.N = 0

    def enQueue(self, value: int) -> bool:
        if self.N == self.k: return False  # 無法再插入
        self.tail += 1  # 尾巴的移動有點特別，先移、再放
        self.queue[self.tail%self.k] = value
        self.N += 1
        return True

    def deQueue(self) -> bool:
        if self.N == 0: return False  # 無法再刪除
        self.head += 1
        self.N -= 1
        return True

    def Front(self) -> int:
        if self.N == 0: return -1  # 沒有東西
        return self.queue[self.head%self.k]

    def Rear(self) -> int:
        if self.N == 0: return -1  # 沒有東西
        return self.queue[self.tail%self.k]

    def isEmpty(self) -> bool:
        return self.N == 0

    def isFull(self) -> bool:
        return self.N == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

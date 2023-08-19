class MyCircularDeque:
    def show(self):
        print(self.nums)
        print("start:", self.start, "end:", self.end, "len:", self.len)
        
    def __init__(self, k: int):
        self.nums = [0]*k
        self.k = k # 大小
        self.start = 0
        self.end = -1 # 預先退一格，因為希望 nums[++end] 讓它對應最後1筆
        self.len = 0

    def insertFront(self, value: int) -> bool:
        if self.len == self.k: return False

        self.start = (self.start + self.k - 1) % self.k # self.start 要往後退
        self.nums[self.start] = value
        self.len += 1
        # self.show()
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k: return False

        self.end = (self.end + 1) % self.k
        self.nums[self.end] = value
        self.len += 1
        # self.show()
        return True

    def deleteFront(self) -> bool:
        if self.len == 0: return False

        self.start = (self.start + 1) % self.k
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0: return False

        self.end = (self.end + self.k - 1) % self.k
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.len == 0: return -1
        return self.nums[self.start]

    def getRear(self) -> int:
        if self.len == 0: return -1
        return self.nums[self.end]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

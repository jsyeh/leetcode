# LeetCode 1429. First Unique Number
# 有一堆整數，找出第1個「unique」的整數
# Queue 裡，照著放入數字，同時有 freq 統計次數
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freq = defaultdict(int)
        self.queue = deque()
        for num in nums:  # 一開始，要把 nums 都加入
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and self.freq[self.queue[0]]!=1:
            # 若能取出 queue 值，但它的freq不是1
            self.queue.popleft() # 就要捨棄

        if self.queue: # 捨棄「非1」的數後，還有剩下，那就是答案
            return self.queue[0]
        return -1

    def add(self, value: int) -> None:
        self.freq[value] += 1  # 加入時，出現次數會+1
        if self.freq[value]==1: # 幸運的 freq為1 時
            self.queue.append(value)  # 就排隊


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

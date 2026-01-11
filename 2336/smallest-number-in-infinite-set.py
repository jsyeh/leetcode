# LeetCode 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.lower = 1  # lower bound of infinite continue set

    def popSmallest(self) -> int:
        if self.heap and self.heap[0]<self.lower:
            ans = heappop(self.heap)
            while self.heap and ans == self.heap[0]:
                heappop(self.heap)
            return ans
        else:
            self.lower += 1
            return self.lower - 1

    def addBack(self, num: int) -> None:
        if num < self.lower:
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# LeetCode 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.smallest = 1
        self.added = set()

    def popSmallest(self) -> int:
        if (not self.heap) or self.smallest <= self.heap[0]:
            ans, self.smallest = self.smallest, self.smallest+1
        else:
            ans = heappop(self.heap)
        self.added.discard(ans) #self.added -= set([ans])
        return ans

    def addBack(self, num: int) -> None:
        if self.smallest > num and num not in self.added:
            heappush(self.heap, num)
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

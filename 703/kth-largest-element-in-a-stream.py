# LeetCode 703. Kth Largest Element in a Stream
# 一開始有一堆數，接著數字一個個餵進來 add(val) 要找到「當時」「第k大」的數。
# 不用 for 迴圈慢慢找。用 heap 資料結構，剛好裡面有k個數（找「最小的數」）
class KthLargest:
    # heap = []  # self.heap 只會放k個數，裡面最小的數，就是「第k大的數」
    # k = 0  # 之後用 self.k 來取用
    def __init__(self, k: int, nums: List[int]):
        self.heap = []  # 可惡，程式會重覆跑，所以每次要清空（這樣第5行、第6行可省略）
        self.k = k  # 記下關鍵的 k（要用 self.k 取用class裡的k)
        for num in nums:  # 慢慢塞入數字
            heappush(self.heap, num)  # 把數字「逐一」塞入 heap
            if len(self.heap)>self.k: heappop(self.heap) # 超過就吐出來
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap)>self.k: heappop(self.heap) # 超過就吐出來
        return self.heap[0]  # heap最前面（k個數中，最小的數）就是第k大的數

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

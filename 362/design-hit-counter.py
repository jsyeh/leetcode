# LeetCode 362. Design Hit Counter
# 每呼叫 hit() 就會增加一次點擊，在 getHits() 時，計算之前5分鐘的點擊次數
class HitCounter:

    def __init__(self):
        self.heap = []  # 利用 heap 資料結構，來存「300秒之內」的時間

    def hit(self, timestamp: int) -> None:
        heappush(self.heap, timestamp)  # 每次 hit() 就存入 heap

    def getHits(self, timestamp: int) -> int:
        while self.heap and timestamp - self.heap[0] >= 300:
            heappop(self.heap)  # 若超過 300 秒時間，就吐掉
        return len(self.heap)  # 最後看剩多少

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

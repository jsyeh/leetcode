# 要發明一個資料結構 & reserve() 和 unreserve(n) 函式, 完成訂位管理任務
# reserve()要取最小的數, 所以要用 priority queue
class SeatManager:

    def __init__(self, n: int):
        self.seat = [i for i in range(1,n+1)]
        heapq.heapify(self.seat) # 將 list 初始化成 heap

    def reserve(self) -> int:
        ans = heapq.heappop(self.seat) # 取出最小的數
        return ans

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seat, seatNumber) # 將 seatNumber塞回heap


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

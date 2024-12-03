# LeetCode 933. Number of Recent Calls
# 電腦網路，有個指令 ping 可看有沒有回應，範圍是3秒內。現在照時間ping
# 問現在t時間，有幾個 ping 還在 3秒內。
class RecentCounter:

    def __init__(self):
        self.queue = deque()  # queue.append() vs. queue.popleft()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0]+3000 < t:  # 如果超過3秒的
            self.queue.popleft()  # 就清掉
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

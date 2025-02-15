# LeetCode 1756. Design Most Recently Used Queue
# 要設計 MRU queue 也就是「最近用過的，要放在最後」
class MRUQueue:

    def __init__(self, n: int):
        self.queue = deque([i for i in range(1,n+1)])
        self.n = n

    def fetch(self, k: int) -> int:
        ans = self.queue[k-1]  # 將 1-index 變回 0-index
        del self.queue[k-1]
        self.queue.append(ans)
        return ans


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

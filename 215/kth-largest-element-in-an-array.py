# 先sorting再做，就超簡單。但題目希望 without sorting。
# 之前用 Java 解是用 PriorityQueue 當heap，逐一加入，再取出
# https://builtin.com/data-science/priority-queues-in-python
from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = PriorityQueue()
        for n in nums:
            heap.put(n)
        for i in range(len(nums)-k+1):
            ans = heap.get()

        return ans

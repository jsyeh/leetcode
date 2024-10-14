# LeetCode 2558. Take Gifts From the Richest Pile
# 從最有錢的那堆，拿禮物，留下「開根號」的結果
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        total = sum(gifts)
        heap = [-gift for gift in gifts]
        heapify(heap)
        taken = 0
        for i in range(k):
            now = -heappop(heap)
            taken += now - int(sqrt(now))
            heappush(heap, -int(sqrt(now)))
        return total - taken

# LeetCode 1962. Remove Stones to Minimize the Total
# 有一堆石頭，堆一堆 piles，每次挑 piles[i], 再從裡面取出 floor(piles/2) 石頭
# 取 k 次後，希望「留下最少的石頭」，也就是「取走最多的石頭」
# 使用 Priority Queue (Heap) 即可，配合「負號」即可。
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]  # 用負號，便能用「最小值」對應「最大值」
        heapify(heap)  # 先把 piles 變成 heap 資料結構
        total = sum(piles)  # 原本有 total 這麼多石頭
        taken = 0  # 取出幾顆石頭
        for i in range(k):  # 重覆 k 次
            now = -heappop(heap)  # 取出最多的那一堆（加「負號」還原）
            taken += floor(now/2)  # 取出的量
            heappush(heap, -(now-floor(now/2)))  # 再把剩下的石頭放回去
        return total - taken

# LeetCode 215. Kth Largest Element in an Array
# 找到 nums 陣列裡「第k大的數」，而且希望「不要用sort」
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)  # 因heapq是先吐出「最小的數」故加負號
        for i in range(k):
            ans = heappop(heap)
        return -ans

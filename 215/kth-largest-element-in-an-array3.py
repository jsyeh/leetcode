# LeetCode 215. Kth Largest Element in an Array
# 找到 nums 陣列裡「第k大的數」，而且希望「不要用sort」
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        for i in range(k):
            ans = heappop(nums)
        return -ans

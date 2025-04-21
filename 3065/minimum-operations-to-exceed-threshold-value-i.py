# LeetCode 3065. Minimum Operations to Exceed Threshold Value I
# 每次可把 nums 裡最小的數刪掉。問「幾次」後，全部的數 >= k
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for num in nums:
            if num < k: ans += 1
        return ans

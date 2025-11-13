# LeetCode 485. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = ones = 0
        for num in nums:
            if num==1:
                ones += 1
            else:
                ans = max(ans, ones)
                ones = 0
        ans = max(ans, ones)
        return ans

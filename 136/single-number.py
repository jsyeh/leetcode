# LeetCode 136. Single Number
# nums 陣列裡「有1個數」只出現1次，找出來 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0  # XOR 的神奇功能：出現2次=沒有出現
        for num in nums:
            ans ^= num
        return ans

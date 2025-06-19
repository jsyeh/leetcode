# LeetCode 1979. Find Greatest Common Divisor of Array
# 找到「最大數、最小數」的「最大公因數」
class Solution:
    def findGCD(self, nums: List[int]) -> int:
            return gcd(max(nums), min(nums))
        

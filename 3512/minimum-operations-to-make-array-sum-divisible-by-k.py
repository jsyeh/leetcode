# LeetCode 3512. Minimum Operations to Make Array Sum Divisible by K
# 每次挑 nums[i] -= 1 要做幾次，可讓「加總結果變k的倍數」 sum(nums) % k == 0
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)  # 全部加起來
        return total % k  # 餘數是多少，就要減幾次

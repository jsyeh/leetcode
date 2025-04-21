# LeetCode 2824. Count Pairs Whose Sum is Less than Target
# 有幾組 nums[i] + nums[j] < target
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i]+nums[j] < target:
                    ans += 1
        return ans

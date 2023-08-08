# 有相同，就是 good pair
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j]: ans += 1
        return ans

# 不同的2個字串「接起來」，和target相同的話，就多1組答案
# 
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            for j in range(N):
                if i==j: continue
                if nums[i]+nums[j]==target: 
                    ans += 1
        return ans

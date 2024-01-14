# 找出 nums[i]==nums[j] 且 i*j%k==0
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            for j in range(i+1,N):
                if nums[i]==nums[j] and i*j%k==0:
                    ans += 1
        return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0]*N
        for i in range(N):
            for k in range(N):
                if i!=k  and nums[i]>nums[k]:
                    ans[i] += 1
        return ans 



class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N-1):
            for k in range(N-1-i):
                nums[k] = (nums[k]+nums[k+1])%10
        return nums[0]

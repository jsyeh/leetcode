class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range (1,N):
            nums[i] = nums[i] + nums[i-1]
        return nums

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        table = [0]*(N+1) # table[i] 表示包含 nums[i] 最長的subarray
        table[0] = nums[0]
        ans = table[0]
        for i in range(1,N):
            table[i] = table[i-1] + nums[i]
            if nums[i] > table[i]:
                table[i] = nums[i]
            if table[i] > ans:
                ans = table[i]
        return ans;

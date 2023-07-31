class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums[0], nums[1])
        table = [0]*N # table[i]表示「包含nums[i]」的最大值
        table[0] = nums[0]
        table[1] = nums[1]
        table[2] = nums[2] + nums[0]
        ans = max(table[1], table[2])
        for i in range(3,N):
            table[i] = max(table[i-2], table[i-3]) + nums[i]
            if table[i] > ans:
                ans = table[i]
        return ans

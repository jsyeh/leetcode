# 有個「產生nums」的規則，有點像Fibonacci的產生法，不過有點不同
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<=1: return n # 解決 nums[0]=0 及 nums[1]=1 的狀況

        nums = [0]*(n+1)
        nums[1] = 1
        ans = 1
        for i in range(2,n+1): # 全部照題目的規則
            if i%2==0: nums[i] = nums[i//2] # 偶數規則
            else: nums[i] = nums[i//2] + nums[i//2+1] # 奇數規則
            ans = max(ans, nums[i])
        return ans

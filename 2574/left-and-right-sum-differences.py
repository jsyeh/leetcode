# leftSum[i] 及 rightSum[i]
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N = len(nums)
        leftSum = [0]*N
        rightSum = [0]*N
        ans = [0]*N
        for i in range(1,N): # 左到右
            leftSum[i] = leftSum[i-1]+nums[i-1]
        for i in range(N-2,-1,-1): # 右到左
            rightSum[i] = rightSum[i+1]+nums[i+1]
        for i in range(N): # 相減絕對值
            ans[i] = abs(leftSum[i]-rightSum[i])
        return ans
        

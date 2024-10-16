# LeetCode 2367. Number of Arithmetic Triplets
# 請問有幾組 i<j<k 使得 nums[i] nums[j] nums[k] 距離 diff
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        N = len(nums)
        for i in range(N-2):  # 用暴力3層 for 迴圈
            for j in range(i+1,N-1):
                for k in range(j+1,N):
                    if nums[j]-nums[i] == diff and nums[k]-nums[j] == diff:
                        ans += 1
        return ans
        

# LeetCode 3038. Maximum Number of Operations With the Same Score I
# 每次能將 nums 前面2個刪掉（對應score是2數相加），只要 score 相同，可一直刪
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        ans = 0
        N = len(nums)
        for i in range(0, N-1, 2):
            if nums[i]+nums[i+1]==score:
                ans += 1
            else:
                break
        return ans

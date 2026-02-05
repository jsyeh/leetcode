# LeetCode 3379. Transformed Array
# 將 nums 陣列繞成圈圈，照 nums[i] 的值「往右or往左」挑到新值
# 因數字不大，照著「模擬往右or往左挑選」即可
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        for i in range(N):
            i2 = (i+nums[i])%N  # 照題目「往右or往左」
            ans[i] = nums[i2]  # 將挑選到的值，放入 ans[i]
        return ans

# LeetCode 259. 3Sum Smaller
# 問有幾種挑法，讓 nums[i] + nums[j] + nums[k] <= target
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()  # 先排序好，會比較好挑數字
        N = len(nums)
        ans = 0
        # 不能用暴力3層for迴圈，因為會超過時間 case 314/316 有一堆30
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if nums[i] + nums[j] + nums[k] < target: ans += 1
                    else: break
        return ans

# LeetCode 259. 3Sum Smaller
# 問有幾種挑法，讓 nums[i] + nums[j] + nums[k] < target
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()  # 先排序好，會比較好挑數字
        N = len(nums)
        ans = 0
        for i in range(N-2):  # 左
            for j in range(i+1, N-1):  # 中
                now = bisect_right(nums, target - nums[i] - nums[j] - 1, lo=j+1) - 1  # 合理的最右界
                ans += max(0, now - j)  # 右 - 中 得到「有幾個可能的位置」
        return ans

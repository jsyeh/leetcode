# LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I
# 將 nums 切成 3 段 subarray，希望3段的「第1個」加起來最小。
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # 因第1段「一定有」 nums[0]
        # 接下來(1) 可用 for 迴圈，試「全部的可能」
        # 或是 (2) sort 找出「最小」的2個，加起來，就是答案
        # 或是 (3) 一層for迴圈，找到最小、次小的2數
        min1, min2 = min(nums[1], nums[2]), max(nums[1], nums[2])  # 最小、次小
        for i in range(3, len(nums)):
            if nums[i]<min1:  # 比「最小」還小
                min2 = min1  # 舊的「最小」變「次小」
                min1 = nums[i]  # 新的「最小」
            elif nums[i]<min2:  # 只比「次小」還小
                min2 = nums[i]  # 新的「次小」
        return nums[0] + min1 + min2  # 三段的「頭」加起來

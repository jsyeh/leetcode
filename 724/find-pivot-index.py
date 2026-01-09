# LeetCode 724. Find Pivot Index
# 想找到「天平的支點」，剛好「左邊加起來」==「右邊加起來
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            if prefix == total - nums[i] - prefix:  # 扣除支點，左半==右半
                return i  # 就找到「支點」了
            prefix += nums[i]  # 沒找到的話，繼續 prefix sum 加下去
        # 離開迴圈，都沒有找到「支點」提早離開，就失敗
        return -1

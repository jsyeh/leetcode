# LeetCode 3432. Count Partitions with Even Sum Difference
# 想將 nums 分段成 0...i 及 i+1...n-1，且「左半、右半」總合「相減」是偶數
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)  # 全部的總合
        if total%2==1: # 總合是奇數，分2段會是「奇、偶」「偶、奇」
            return 0  # 相減的話，一定是奇數，所以「沒有可能的答案」
        # 接下來，可分成「偶、偶」「奇、奇」，隨便相減都能得到偶數
        # 所以 n 個數，有 n-1 種分法，都正確
        return len(nums) - 1

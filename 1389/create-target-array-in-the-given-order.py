# LeetCode 1389. Create Target Array in the Given Order
# 將 nums[i] 照著 index[i] 的位置，插入 target 陣列裡
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        N = len(nums)
        target = []
        for i in range(N):
            ii = index[i]  # 要插入的 index 位置
            target = target[:ii] + [nums[i]] + target[ii:]
            # 舊的 target 拆成 target[:ii] 和 taget[ii:] 中間插入 nums[i]
        return target

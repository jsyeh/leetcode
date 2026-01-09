# LeetCode 283. Move Zeroes
# 要 in-place 移到 nums 裡的數，將 0 移到右邊
# 其他數「照原本順序」移到左邊
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = end = 0  # 目前收集到幾個0、持續放數字的位置 end
        for i in range(len(nums)):
            if nums[i]==0: 
                zeros += 1  # 遇到0
            else:  # 不是0的話，放到 end 位置
                nums[end] = nums[i]
                end += 1
        for i in range(end, len(nums)):
            nums[i] = 0  # 後面都放0

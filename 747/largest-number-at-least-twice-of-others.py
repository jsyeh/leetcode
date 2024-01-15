# 找「最大數」，且要比別人「大兩倍」
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = nums[0]
        ansI = 0
        for i,num in enumerate(nums): # 先找最大值
            if num>largest: # 找到最大值對應的 index
                largest = num # 更新
                ansI = i # 更新
        for i,num in enumerate(nums):
            if i!=ansI and largest<num*2: # 不夠大
                return -1 # 就失敗了
        return ansI 

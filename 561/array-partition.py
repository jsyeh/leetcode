# 將數字兩兩一組，問「把組中小的」加起來的「最大值」
# 可以排序後，再由大到小 不挑、挑、不挑、挑 一直做下去
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() # 從小到大排好
        ans = 0
        for i in range(0,len(nums), 2): # 由小到大，兩兩一組
            # 挑小，不挑大，一直做下去
            ans += nums[i]
        return ans

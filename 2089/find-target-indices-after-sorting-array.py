# 想找出 sorted 後 nums[i]==targt 的數
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort() # 題目說，要先 sort
        ans = []
        for i,now in enumerate(nums): # 再把全部的 nums[i]==target 的 i 存起來
            if now==target: ans.append(i)
        return ans

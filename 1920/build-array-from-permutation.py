# LeetCode 1920. Build Array from Permutation
# 題目說 ans[i] = nums[nums[i]] 就照著寫，就好了
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
        # 利用倒裝句，把每個 i 對應的 nums[nums[i]] 準備好，就成功了
        

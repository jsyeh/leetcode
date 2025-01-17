# LeetCode 3173. Bitwise OR of Adjacent Elements
# 請找出 ans[i] = nums[i] | nums[i+1] 的陣列
class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):  # 要少1個，因為下面有 nums[i+1]
            ans.append( nums[i] | nums[i+1] )
        return ans

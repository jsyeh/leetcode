# nums 沒有排序過，找到 middleIndex 使得
# nums[0]+...+nums[middleIndex-1] =＝右邊加起來
# 因為數字很小，就用暴力法即可。如果想要快一點，可以用 prefix 及 postfix 做比較
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)): # 全部暴力去試
            if sum(nums[:i])==sum(nums[i+1:]): # 左右相等
                return i # 找到答案
        return -1

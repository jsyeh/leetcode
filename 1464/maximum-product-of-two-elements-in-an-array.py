# 這是12月超簡單的題目
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0 # 用來放答案的變數
        N = len(nums) # nums 這個陣列 list 有幾個數
        for i in range(N): # 左手 i 
            for j in range(i+1, N): # 右手 j 
                ans = max(ans, (nums[i]-1) * (nums[j]-1) ) # 照題目去找相乘的最大值
        return ans

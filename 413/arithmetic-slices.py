# 「連續3個以上」的「等差數列」有幾個
# 其實就逐個去比較，就能算出來了
# 配合 Dynamic Programming 去更新 table[i] 對應它之前成立的可能性有幾個
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        table = [0]*N # table[i] 表示 nums[i]結尾的等差數列有幾個
        for i in range(2,N): # 要往前比[i-1] 及 [i-2] 兩項
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]: # 是等差
                table[i] += table[i-1] + 1 # 前面有幾種，就再加這些可能性
                ans += table[i] # 這些可能性，都算進來
        return ans

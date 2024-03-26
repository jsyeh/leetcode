# 有一堆連續的數字，要找到缺的數字
# 因為數字很少，只有50個數字，所以簡單。
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # 先找 連續數字的prefix sum
        prefix = nums[0] # 放 前 i 項的加總結果
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1: # 還是連續的數字
                prefix += nums[i]
            else: # 如果沒有連續的數
                break # 就離開，再找下一個數字
        # 找下一個數字
        ans = prefix # 從 prefix sum 開始，逐一檢查
        while ans in nums: ans += 1
        return ans

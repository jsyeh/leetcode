# 如果左小右大，可把 nums[i] 及 nums[i+1] 合併起來
# 但 nums 有 10^5 項，不能用暴力for迴圈去模擬
# 查看 Solutions 裡 HoneyJammer 的解法，用反過來的迴圈，逐項加回來，還蠻好的
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        N = len(nums)
        ans = nums[N-1] # 先隨便拿個值來放，拿最右邊那個，因迴圈漏看它
        for i in range(N-2,-1,-1): # 倒過來的迴圈
            if nums[i]<=nums[i+1]: # 照規定可合併
                nums[i] += nums[i+1] # 等價於 += nums[i+1]
            ans = max(ans, nums[i]) # 找陣列裡的最大值
        return ans

# LeetCode 1493. Longest Subarray of 1's After Deleting One Element
# nums 陣列裡，「如果必須刪掉1個數」之後，「只有1」的subarray最長有多長？
# 看起來就用「毛毛蟲」的方法來解，肚子裡要「剛好有1個0」才行。但如果都沒有0，那只能刪1個1
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        tail = 0  # 毛毛蟲的尾巴位罝
        zero = 0  # 目前「毛毛蟲」的身體裡，有幾個 0
        ans = 0  # 答案（最長的 subarray 長度）
        for head in range(len(nums)):  # 毛毛蟲的頭，持續往右進
            if nums[head]==0: zero += 1  # 頭部吃到 0
            while zero > 1:  # 若身體裡，有超過 1 個 1，尾巴就要一直吐
                if nums[tail]==0: zero -= 1. # 吐掉的是 0，很好，減1
                tail += 1
                
            # 下面4行，其實可以簡化成一行： ans = max(ans, head - tail)
            if zero==1:  # 剛好有1個0可被刪掉
                ans = max(ans, head - tail)  # 扣掉1個0之後的長度
            elif zero==0:  # 沒有0可以刪的話
                ans = max(ans, head - tail)  # 扣掉1個1之後的長度
        return ans

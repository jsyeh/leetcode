# LeetCode 1493. Longest Subarray of 1's After Deleting One Element
# nums 陣列裡，「如果必須刪掉1個數」之後，「只有1」的subarray最長有多長？
# 看起來就用「毛毛蟲」的方法來解，肚子裡要「剛好有1個0」才行。但如果都沒有0，那只能刪1個1
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = j = 0
        zeros = 0
        ans = 0
        while j < len(nums):
            zeros += (nums[j]==0)
            while zeros > 1:
                zeros -= (nums[i]==0)
                i += 1
            ans = max(ans, (j-i+1) - 1 )  # 一定要扣掉1個數
            j += 1
        return ans

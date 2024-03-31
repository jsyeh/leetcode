# 有幾種 subarray, 最小值剛好是 minK, 最大值剛好是 maxK
# 我之前是參考 vikas007 的方法。這次打算參考 lee215 的作法
# 應該還是用毛毛蟲的作法，不過如果 nums[i] 超過範圍，就作廢
# 記下最小值是minK的位置left2、最大值是maxK的位置left1。
# 要避開 bad 的位置left3。
# left3...left2...left1....right
#      ^^^ possible 可能的範圍
# left3...left1...left2....right
#      ^^^ possible 可能的範圍
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        left1 = left2 = left3 = -1
        for right in range(len(nums)):
            if nums[right]>maxK or nums[right]<minK: # 壞掉
                left3 = right # 敗壞的，不能包含它
            if nums[right]==maxK: left1 = right
            if nums[right]==minK: left2 = right
            possible = min(left1,left2)-left3 # 這輪right對應「可能」的範圍
            if possible>0: ans += possible
        return ans


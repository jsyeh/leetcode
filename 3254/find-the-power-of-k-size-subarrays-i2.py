# LeetCode 3254. Find the Power of K-Size Subarrays I
# 陣列power：如果「陣列小到大、間隔差1」就挑最大那個，不然就-1
# 請把長度為k的subarray的「陣列power」都算出來
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # 用比較厲害的sliding window法，記下「之前累積幾個combo」
        ans = []
        combo = 0
        for i in range(k-1): # 先看看第1組，有沒有順利combo
            if nums[i] + 1 == nums[i+1]:
                combo += 1  # 相鄰差1，combo
            else:
                combo = 0
        if combo >= k-1: ans.append(nums[k-1])
        else: ans.append(-1)

        for i in range(k,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                combo += 1
            else: combo = 0
            if combo >= k-1: ans.append(nums[i])
            else: ans.append(-1)
        return ans

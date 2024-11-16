# LeetCode 3254. Find the Power of K-Size Subarrays I
# 陣列power：如果「陣列小到大、間隔差1」就挑最大那個，不然就-1
# 請把長度為k的subarray的「陣列power」都算出來
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # 用比較厲害的sliding window法，記下「之前累積幾個combo」
        ans = []
        combo = 0
        if k==1: ans.append(nums[0])  # 若k是1，下面迴圈沒考慮到，所以補丁

        for i in range(1,len(nums)):  # 從1開始，逐一檢查：有沒有順利combo
            if nums[i-1] + 1 == nums[i]: combo += 1  # 相鄰差1，combo
            else: combo = 0  # 重新累積 combo
            
            if i >= k-1:  # 開始能連續 k-1 combo 項 (有 k項 0...k-1)
                if combo >= k-1: ans.append(nums[i])  # 累積的 combo 數足夠
                else: ans.append(-1)
        return ans

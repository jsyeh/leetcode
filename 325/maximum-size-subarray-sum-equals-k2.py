# LeetCode 325. Maximum Size Subarray Sum Equals k
# nums 陣列裡，加起來是 k 的連續 subarray 最長有多長？
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = 0  # 用來知道 0...i 的累積和
        pos = {0:-1}  # 曾經出現過的 prefixSum 的位置
        ans = 0
        for i, num in enumerate(nums):
            prefixSum += num  # 累積和
            if prefixSum - k in pos:  # 若曾出現過「適當的數」
                ans = max(ans, i - pos[prefixSum - k])  # 更新「最長距離
            if prefixSum not in pos:  # 若之前沒出現過
                pos[prefixSum] = i  # 記錄這個位置
        return ans

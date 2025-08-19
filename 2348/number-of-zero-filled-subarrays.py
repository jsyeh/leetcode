# LeetCode 2348. Number of Zero-Filled Subarrays
# 有幾種 subarray 裡面都是 0
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        combo = 0  # 目前「有連續幾個0」
        for num in nums:
            if num==0: combo += 1  # 繼續增加0的個數
            else: combo = 0  # 現在沒有0了
            ans += combo  # 重點在這行
            # 現在 num 結束的位置，有連續combo個0，可拉出combo個 subarray
        return ans
        

# LeetCode 3381. Maximum Subarray Sum With Length Divisible by K
# 在一堆「長度是k的倍數」的subarray裡，subarray內容加起來最大是多少？
# 當「開始、結束位置」都是 %k 同餘，就是我們的「候選人」
# 「記下%k餘數」最小的presum再相減即可
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prev = {k-1:0}  # 對照表，了解「位置%k同餘」的最小值，以便相減得最大值
        # 這個k-1對應「什麼都沒有」時的preSum值，剛好是0
        preSum = 0  # 累積的 preSum 值，希望 preSum - prev[i%k] 得到最大值
        for i in range(k-1):  # 先把前面 k-1 項的 preSum 值，都加入 prev[i] 裡
            preSum += nums[i]  # 累積
            prev[i] = preSum  # 將「累積」存入 prev[i]
        ans = -inf  # 要找「最大值」，所以預設值「-inf最小」
        for i in range(k-1, len(nums)):  # 開始要累積「前k項」的和（0...k-1剛好k項）
            preSum += nums[i]  # 累積
            ans = max(ans, preSum - prev[i%k])  # 更新答案
            prev[i%k] = min(prev[i%k], preSum)  # 將「累積」更新 prev[i]
        return ans

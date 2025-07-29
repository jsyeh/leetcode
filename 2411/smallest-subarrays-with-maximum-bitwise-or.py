# LeetCode 2411. Smallest Subarrays With Maximum Bitwise OR
# nums 陣列裡，算出「每個位置開始」的 subarray (往右)能達到最大 OR 結果的「最小長度」
# ex. [7, 1, 1] 這個陣列，最左邊7開始「往右滑」最大也只能到7，所以長度1
# 中間1開始「往右滑」最大也只能到1，所以長度1 。右邊1開始「往右滑」最大也只能到1，所以長度1
class Solution:  # 這題我模仿 lee215 的解法
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # 可倒過來看：每個bit「最近一次是1」的index在哪裡(lastPos) -- 為了「subarray OR 最大」就要包含它
        nearestBitIndex = [0] * 32  # 32個 bits 每個 bit 最近是 1 的 index
        ans = [1] * len(nums)  # nums 有幾個，ans 就有幾個（每一個都要找到對應的長度）
        for i in range(len(nums)-1, -1, -1):  # 倒過來的迴圈，從右往左「慢慢更新」
            lastPos = 0  # index i 到最後「曾出現的 bit 值是1」全部包含的最近的位置
            for b in range(32):  # 32 bits 逐一檢查，現在檢查第 b 個 bit
                if nums[i]>>b & 1:  # 對應的 bit 有值，可更新 bit b
                    nearestBitIndex[b] = i  # 這個 bit b 在 index i 有出現
                lastPos = max(lastPos, nearestBitIndex[b])  # 「曾出現的 bit 值是1」的最近的最右邊
            ans[i] = max(1, lastPos - i + 1)  # 從 index i 到 index lastPos 的長度
            # 為了怕 lastPos 是 0 的話「會有負數」就放「自己本身」的長度為1即可
        return ans  # 全部的答案

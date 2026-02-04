# LeetCode 3640. Trionic Array II
# 將 nums 取出一段小陣列，裡面符合「升、降、升」希望「加起來最大」
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ans = -inf  # 要找「最大值」，「答案」初始值就設成「最小的 -inf」以便更新
        i = 1  # 迴圈從 1 開始，從常見的 for i in range(1,len(nums) 迴圈
        while i < len(nums):  # 改成 while 迴圈的寫法
            if nums[i-1] > nums[i]:  # 一旦遇到有「下降」，就開始「分析」
                p = i-1  # 備份「下降」時的 local 最高點 index p
                now = nums[i-1]  # 先累積「下降段」的加總，「全部」加起來
                while i < len(nums) and nums[i-1] > nums[i]:  # 持續「往下滑動」
                    now += nums[i]  # 順手將「下降段」的 nums[i] 全部加入 now
                    i += 1  # 往右的迴圈，用 i 當 index
                if p-1>=0 and i<len(nums) and nums[p-1]<nums[p] and nums[i-1]<nums[i]:
                    # 前面是「升」、後面也是「升」往上翹，可往前、往後分析
                    maxPreSum, preSum = -inf, 0  # 用 prefix sum 技巧，記錄「每一段」的加總
                    while p-1 >= 0 and nums[p-1]<nums[p]:  # 往左的迴圈，用 p 當 index
                        preSum += nums[p-1]  # 累加左端的值
                        maxPreSum = max(maxPreSum, preSum)  # 更新 prefix sum
                        p -= 1  # 往左的迴圈，用 p 當 index
                    now += maxPreSum
                    maxPreSum, preSum = -inf, 0  # 用 prefix sum 技巧，記錄「每一段」的加總
                    while i < len(nums) and nums[i-1]<nums[i]:  # 往右的迴圈，用 i 當 index
                        preSum += nums[i]  # 累加右端的值
                        maxPreSum = max(maxPreSum, preSum)  # 更新 prefix sum
                        i += 1  # 往右的迴圈，用 i 當 index
                    now += maxPreSum
                    ans = max(ans, now)  # 最後「更新答案」
            else: i += 1  # 沒有遇到「分析」，就簡單 i += 1 讓迴圈繼續
        return ans

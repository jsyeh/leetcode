# LeetCode 2461. Maximum Sum of Distinct Subarrays With Length K
# 長度 k 的 subarrays （裡面每格都不同）加起來最大值。連續subarray適合「毛毛蟲」
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0  # 如果都不符合，要回傳 0
        counter = Counter()  # 可用 Counter() 來看大家是否都為1
        unique, total = 0, 0  # 目前這段k個數，有幾個不同的數、加總值
        for i in range(k):  # 先算出第1段的 uniquie 及 total 值
            now = nums[i]  # 我習慣用 now 代表現在的 nums[i] 讓程式易懂
            counter[now] += 1
            if counter[now]==1: unique += 1  # 從0變1，多1個unique
            if counter[now]==2: unique -= 1  # 從1變2，少1個unique
            total += now  # 更新 total
        if unique==k: ans = max(ans, total)  # 符合條件，才更新
        # 利用「毛毛蟲」sliding window 更新
        for i in range(k, len(nums)):
            left, right = nums[i-k], nums[i]  # 左邊要吐、右邊要吃
            counter[left] -= 1  # 吐左邊
            if counter[left]==1: unique += 1  # 從2變1，多1個unique
            if counter[left]==0: unique -= 1  # 從1變0，少1個unique
            counter[right] += 1  # 吃右邊
            if counter[right]==1: unique += 1  # 從0變1，多1個unique
            if counter[right]==2: unique -= 1 # 從1變2，少1個unique
            total = total + right - left  # 更新 total
            if unique==k: ans = max(ans, total)
        return ans

# LeetCode 2461. Maximum Sum of Distinct Subarrays With Length K
# 長度 k 的 subarrays （裡面每格都不同）加起來最大值。連續subarray適合「毛毛蟲」
# 策略：「只要吃到『重覆』」，就要一直吐，吐到「沒有重覆」腸子清空為止。
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0  # 最後的答案
        total = 0  # 目前毛毛蟲 sliding window 裡的總和
        window = set()  # sliding window 裡面有「目前吃到肚子裡」的數（都必須是unique）
        left = 0  # 毛毛蟲的左邊界
        for right in range(len(nums)): # 毛毛蟲的右邊界，慢慢遞增
            while nums[right] in window or len(window)>=k:  # 將吃的「右邊」已在肚子裡，或長度太長
                window.remove(nums[left])  # 就一直吐「左邊」，直到肚子清空、沒「將加入」的數
                total -= nums[left]  # 吐掉時，total也變小
                left += 1
            # 現在吐得很乾淨，沒有重覆的數，才能將「右邊」安全的加入
            window.add(nums[right])  # 吃「右邊」
            total += nums[right]  # total 變大
            if len(window)==k:  # 若有幸「長度剛好是k」
                ans = max(ans, total)
        return ans            

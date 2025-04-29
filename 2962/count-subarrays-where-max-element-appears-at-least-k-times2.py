# LeetCode 2962. Count Subarrays Where Max Element Appears at Least K Times
# 數一數，有多少種 subarray 裡面有 nums 的最大值「出現k次」
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = tail = times = 0
        # 答案、毛毛蟲的尾巴、出現「最大值」的次數
        maximum = max(nums)  # 最大值
        for head in range(len(nums)):  # 毛毛蟲的頭，慢慢往右移
            if nums[head] == maximum: times += 1  # 吃到最大值」
            while times >= k:  # 希望毛毛蟲尾巴在「剛好不足k個」處
                if nums[tail] == maximum: times -= 1  # 吐出最大值
                tail += 1  # 尾巴往右縮
            ans += tail  # 尾巴在「剛好不足k個」，0...tail-1 都足k個
        return ans

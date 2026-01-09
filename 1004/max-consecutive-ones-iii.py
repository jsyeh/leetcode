# LeetCode 1004. Max Consecutive Ones III
# 最多的連續1 --- 如果你能把 nums 裡把k個0變成1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 使用毛毛蟲技巧，肚子裡「最多有k個0」超過就要從左邊尾巴吐掉
        tail = 0
        zeros = 0
        ans = 0
        for head in range(len(nums)):
            if nums[head]==0: zeros += 1
            while zeros > k:
                if nums[tail]==0: zeros -= 1
                tail += 1
            ans = max(ans, head - tail + 1)
        return ans

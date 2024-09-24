# LeetCode 3095. Shortest Subarray With OR at Least K I
# 希望 subarray 裡的數 OR 起來後 >=k，問最小的subarray裡，有幾個數
# subarray 是連續的 nums[i]...nums[j]
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        N = len(nums)
        for i in range(N):
            now = 0
            for j in range(i,N):
                now |= nums[j]  # 把i..j的每個數，都OR合起來
                if now >= k:  # 若合規定
                    ans = min(ans, j-i+1)  # 就更新答案
        if ans==inf: return -1
        else: return ans


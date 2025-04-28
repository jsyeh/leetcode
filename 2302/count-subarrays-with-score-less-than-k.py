# LeetCode 2302. Count Subarrays With Score Less Than K
# nums 有幾組 subarray 裡面的「各數相加，再乘長度 <k」
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = total = tail = 0  # 初始值
        for head in range(len(nums)):
            total += nums[head]  # 右邊頭吃1個數
            while total * (head-tail+1) >= k:  # 若乘出來的數太大
                total -= nums[tail]  # 左邊尾巴吐1個數
                tail += 1  # 移動尾巴的數目
            ans += head-tail+1  # 右端是 head，左邊可以是 tail ... head 
            # 共增加 head-tail+1 種可能
        return ans

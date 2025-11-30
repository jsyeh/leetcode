# LeetCode 1590. Make Sum Divisible by P
# 希望 nums 裡「移除最短的subarray」讓 sum(nums) % p ==0
# 所以目標其實是「找到 subarray」的和是 target 即可
# 做對照表，快速找到「相減的餘數是p」的位置 即可解此題。
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p  # 希望 subarray 的餘數是 target 即可
        if target==0: return 0  # 太好了，可整段用，不用移除任何 subarray
        prev = {0:-1}  # 前一次出現「某個」餘數的位置
        ans = inf  # 想找最小的長度
        now = 0  # running sum
        for i in range(len(nums)):
            now += nums[i]  # nums[0]...nums[i] 的 running sum
            mod = (now - target + p) % p  # 現在餘 - target 即「之前的餘」
            if mod in prev:  # 若曾出現餘數 mod 代表「有機會湊出target」
                ans = min(ans, i - prev[mod])
            prev[now%p] = i  # 記錄這次的餘數，對應的位置i
        if ans==inf or ans==len(nums): return -1  # 不能全刪哦！
        return ans

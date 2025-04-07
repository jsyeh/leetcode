# LeetCode 416. Partition Equal Subset Sum
# 能否把 nums 分兩群「個自加起來」相同？
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2==1: return False  # 奇數無法「平分兩堆」
        N = len(nums)
        @cache
        def helper(target, i):  # 「挑、不挑」看能否湊到「剛好一半」的target
            if target==0: return True
            if i>=N or target<0: return False
            return helper(target, i+1) or helper(target-nums[i], i+1)
        return helper(total//2, 0)
        # 下面是 O(2^n) 會超過時間，所以換上面的解法
        @cache  # 利用 Dynamic Programming 函式呼叫函式，試各種可能
        def helper(target, i):  # 可試「有正有負」nums可湊到哪些數
            if i >= N and target==0: return True
            if i >= N and target!=0: return False
            if helper(target + nums[i], i+1) or helper(target - nums[i], i+1): return True
            return False
        return helper(0, 0)

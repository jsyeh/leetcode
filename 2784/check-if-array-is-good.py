# LeetCode 2784. Check if Array is Good
# nums 能不能由 base[n] 做出來
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()  # 先「從小到大」排好
        n = len(nums)-1  # 1...n 加上 n
        for i in range(n):  # 檢查 [1...n] 的部分
            if nums[i] != i+1: return False  # 不符合，就失敗
        return nums[n] == n  # 最後的數，必須是 n

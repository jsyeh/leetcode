# LeetCode 2294. Partition Array Such That Maximum Difference Is K
# nums 陣列「拆成幾分」，裡面「最大值-最小值 <= k」
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()  # 先「小到大」排好，便能依序檢查「能不能放在同一群」
        start = nums[0]  # 開始的最小的數
        ans = 1  # 現在從 start 開始，收集「第一群」數字
        for i in range(len(nums)):  # 逐一檢查
            if nums[i] - start <= k:
                continue  # 還能「包含」在「同一群」裡，繼續收集
            else:  # 不能「包在同一群」裡，就要「開新的一群」
                start = nums[i]  # 新的開始
                ans += 1  # 換「新的一群」
        return ans  # 總共分了這麼多群

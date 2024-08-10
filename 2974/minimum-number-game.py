# LeetCode 2974. Minimum Number Game
# 一堆數字 nums, 兩人依序取出「最小數」，再倒著放回 arr 裡。
# 所以其實 sort() 後，再「兩兩交換」即可
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()  # 先小到大排好
        for i in range(0, len(nums), 2):  # 兩兩交換
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

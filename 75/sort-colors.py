# LeetCode 75. Sort Colors
# nums 裡只有 0, 1, 2 三種數，不呼叫 sort()把它們排好
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)  # 先數一下，統計 0, 1, 2 的個數 
        a, b, c = counter[0], counter[1], counter[2]  # 數量
        nums[:a], nums[a:a+b], nums[a+b:] = [0]*a, [1]*b, [2]*c
        # 照著3段的位置，依序放「一堆0」「一堆1」「一堆2」

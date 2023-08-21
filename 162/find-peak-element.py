# 全部巡一次，就可找到任一個 peak element
# 不過題目希望用 O(log n) 找到。任一個local maximum 就可以。可用斜率法來做
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 先把邊界條件解決
        N = len(nums)
        if N == 1: return 0
        if nums[0] > nums[1]: return 0 # 最左邊的極端case先處理掉

        # 口訣：斜率向右，則右邊有peak。斜率向左，則左邊有 peak
        left, right = 1, N # 因為要比較 nums[i-1] 和 nums[i]
        while left < right:
            mid = (left+right)//2
            if nums[mid-1] > nums[mid]:
                right = mid
            else: # 題目保證 nums[i] != nums[i+1]
                left = mid + 1
        return left-1
# case 2/66: [1]

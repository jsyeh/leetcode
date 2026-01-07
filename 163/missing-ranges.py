# LeetCode 163. Missing Ranges
# 在 [lower, upper] 範圍內，放 nums 裡的數，會有一些範圍miss掉
# 找出這些 miss 掉的小範圍
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        for num in nums:
            if num != lower:  # 開始有漏的數了
                if lower <= num-1: ans.append([lower, num-1])
                lower = num + 1
            else:  # 有出現數字了，連續
                lower = num + 1
        if lower <= upper:
            ans.append([lower, upper])
        return ans

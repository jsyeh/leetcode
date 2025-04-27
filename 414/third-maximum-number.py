# LeetCode 414. Third Maximum Number
# 在 nums 裡找到「第3大」的數。但如果沒有「第3大」的數，那就找到「最大」的數
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -inf  # 都先設成「最小」的數
        for num in nums:
            if num==first or num==second or num==third:
                continue  # 重覆的數，不要進行比較
            if num > first:  # 比最大還大，依序更新
                first, second, third = num, first, second
            elif num > second:  # 比第2大還大
                second, third = num, second
            elif num > third:  # 比第3大還大
                third = num
        # 題目說，若無「第3大」的數，就回傳「最大」的數
        if third == -inf:
            return first
        return third

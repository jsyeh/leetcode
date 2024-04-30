# subsequence 是「刪掉一些」的結束，不改順序。
# 想找到 All Subsequences Sums 的 bitwise OR 結果
# 看起來和加法的「進位」有關係。我想到一個方法，就是邊加邊 OR
# 答案就是「逐個OR」的結果
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = 0
        total = 0
        for num in nums:
            total += num
            ans |= num
            ans |= total
        return ans


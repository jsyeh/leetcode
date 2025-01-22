# LeetCode 2529. Maximum Count of Positive Integer and Negative Integer
# 找出「有幾個正數」「有幾個負數」，大的那個數量回傳
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for num in nums:
            if num<0: neg += 1
            if num>0: pos += 1
        return max(neg, pos)

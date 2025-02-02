# LeetCode 1752. Check if Array Is Sorted and Rotated
# 想確認 nums 裡，是否是「有排序好」可接受「稍微轉動」的結果 
# ex. 3,4,5,1,2就是好的。觀察發現相鄰兩兩比較，最多只會發生一次逆轉。
class Solution:
    def check(self, nums: List[int]) -> bool:
        bad = 0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]: bad += 1
        return bad <= 1

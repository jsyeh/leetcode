# 這題，是把 nums 裡的每個數「先平方」再排序好。
# 我用一行解出來，開心 :)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num*num for num in nums])

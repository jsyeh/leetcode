# LeetCode 1929. Concatenation of Array
# 把陣列複製2次
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [num for num in nums]
        for num in nums:
            ans.append(num)
        return ans

# 好久不見，超喜歡 Easy 題！
# 題目給 nums[i]，問你「裡面有幾個數，剛好>=那個數」
# 比如說：有1個數，剛好>=1 。或是有3個數，剛好>=3 。找出那個數
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left, right = -1, len(nums)
        while left<=right:
            x = (left+right) // 2
            now = 0
            for num in nums:
                if num >= x: now += 1
            if now==x: return x
            if now>x: left = x + 1
            else: right = x - 1
        return -1


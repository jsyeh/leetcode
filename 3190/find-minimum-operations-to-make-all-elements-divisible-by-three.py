# LeetCode 3190. Find Minimum Operations to Make All Elements Divisible by Three
# 每次可將 nums 裡的數「挑1個數」加1 or 減1，問最少要幾次，才能全部變「3的倍數」
# 剛好這麼巧，任何數 % 3 可以餘0、餘1、餘2，而餘1的數「減1」、餘2的數「加1」就成功
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0  # 所以只要數一下，有幾個數「不合格」，各做1次就都能合格
        for num in nums:  # 逐一檢查每個數
            if num % 3 != 0: ans += 1  # 不合格的數有幾個
        return ans

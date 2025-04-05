# LeetCode 1863. Sum of All Subset XOR Totals
# 「排列組合」的題目，從 nums 挑出來的數「全部XOR起來」
# 把「所有可能挑選的方法」的「全部XOR起來」的結果「加起來」當答案
# 速解法：某個數要挑它，有 2的(N-1)種可能；某個 bit 有值的話，也是 2的(N-1)種可能
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0  # 答案對應的「某個 bit」會不會「打開」呢？
        for num in nums:
            ans |= num  # 用 OR 運算，確認「有哪些bit」有牽扯到
        N = len(nums)  # 有 N 個數
        return ans * (2**(N-1))  # 所以算出來的答案，要再乘 2的(N-1)次方

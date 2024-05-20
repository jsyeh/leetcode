# LeetCode 1863. Sum of All Subset XOR Totals
# XOR total 是把每個 nums[i] 都用 XOR 合起來。
# 把 nums[i] 的各種組合，都 XOR 起來，再加起來，答案是多少？
# 會是 Easy 題，代表有速解法，程式特別簡單。但怎麼從題目找到秘訣/解法呢？
# 可觀察 Example 的模擬示範。只有12個數，排列組合最多 2^12＝4096種可能
# 先把全部組合的可能性，都暴力做過一次即可。
# 然後，參考別人「更快」的答案，發現「速解法」：2**(n-1) * bitORSum
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)  # 總共有 N 個數
        bitORSum = 0
        for num in nums:  # 把全部的數，先 OR 起來，得到 bitORSum 
            bitORSum |= num
        return bitORSum * (2**(N-1))  # 有很多倍

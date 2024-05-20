# LeetCode 1863. Sum of All Subset XOR Totals
# XOR total 是把每個 nums[i] 都用 XOR 合起來。
# 把 nums[i] 的各種組合，都 XOR 起來，再加起來，答案是多少？
# 會是 Easy 題，代表有速解法，程式特別簡單。但怎麼從題目找到秘訣/解法呢？
# 可觀察 Example 的模擬示範。只有12個數，排列組合最多 2^12＝4096種可能
# 所以，把全部組合的可能性，都暴力做過一次即可。
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)  # 總共有 N 個數
        ans = 0  # 最後加起來的結果
        for mask in range(2**N):  # 全部的排列組合, 若12個數，就2^12
            xor_total = 0  # XOR total 的結果放這裡
            for i in range(N):  # 逐個 bit 處理，看nums[i]要不要用
                if mask & (1<<i) != 0:  # mask的i個bit亮：用到nums[i]
                    xor_total ^= nums[i]  # 就 XOR 算進來
            ans += xor_total  # 再加起來
        return ans

# LeetCode 1863. Sum of All Subset XOR Totals
# 「排列組合」的題目，從 nums 挑出來的數「全部XOR起來」
# 把「所有可能挑選的方法」的「全部XOR起來」的結果「加起來」當答案
# 註：XOR 運算像「加法」也像「減法」，可把 bit 打開或關起來
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0  # 用暴力法，試看看
        N = len(nums)  # 總共有 N 個數字，全部可能的挑法有 2^N
        for bitMask in range(2**N):  # 使用 bitMask 技巧，來挑數字
            now = 0  # 這次挑的數字「全部XOR起來」的結果是什麼？
            for i in range(N):  # 這次「挑數字」挑到哪幾個數？
                if bitMask & (1<<i):  # 用 AND 運算，看第 i 個數有沒有挑到
                    now ^= nums[i]  # 把「挑中的數字」XOR 進來
            ans += now  # 把這次 bitMask 挑出來的數的XOR結果，加入 ans
        return ans

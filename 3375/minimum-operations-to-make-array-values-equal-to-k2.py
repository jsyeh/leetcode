# LeetCode 3375. Minimum Operations to Make Array Values Equal to K
# 每次可在 nums 挑個 valid 的數 h，比它大的數(都要相同)，都會變成 h
# 要讓 nums 裡全部的數都變成 k，最少要幾步？
# 等價：如果把數字「小到大」排好，有幾個「不同」的數？要退幾步，才會變成k
# 等價：要切幾刀, 才能把數字全部變成 k (也就是 「k 以上, 有幾種不同的數字」)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        s = set(nums)  # 有幾個不同的數
        if k in s: return len(s) - 1  # 若 set 裡有 k，那要避開它，才會得到「k 以上」
        else: return len(s)  # 若沒有 k，就全部都是「k 以上」不同的數

# LeetCode 1611. Minimum One Bit Operations to Make Integers Zero
# 目標：把 n 變成 0，需要幾步？ 每步可有兩種操作：(1) 改變二進位「最右邊bit」 
# (2) 若二進位有個bit的右邊「有個1，再右方全是0」可將那個bit改綊
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def helper(n):
            if n==0: return 0  # 函式呼叫函式，一定要有「終止條件」0是0步可到0
            b = 1  # 用 b 建出「左邊有個1、右邊都是0」的數
            while (b<<1) <= n:  # n 像是 10101 之類的數 
                b = b << 1  # 這是要建出 100000 之類「比 n 大」右邊都是0的數
            bb = b + (b>>1)  # 這是要建出110000 左邊有2個1的數，
            part1 = helper(n ^ bb) + 1  # 大問題「拆成小問題」，位數變小
            part2 = b - 1  # 這個公式，把 10000 變成 0 的步數
            return part1 + part2
        return helper(n)

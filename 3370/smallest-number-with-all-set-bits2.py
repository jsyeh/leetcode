# LeetCode 3370. Smallest Number With All Set Bits
# 從 n 開始往上找, 找到到「2進位表示時, 全部都是1」的數
class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        while n>0:  # 利用「剝皮法」
            n = n // 2  # 把 n 以「二進位」風格剝皮
            ans = ans * 2 + 1  # 逐步「組出」一堆1的數
        return ans

# LeetCode 3370. Smallest Number With All Set Bits
# 從 n 開始往上找, 找到到「2進位表示時, 全部都是1」的數
class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1
        while n>0:  # 利用「剝皮法」
            n = n // 2  # 把 n 以「二進位」風格剝皮
            ans *= 2  # 每次多1位數，ans就多1位（多1個0）
        return ans - 1  # 利用「計算機概論」2的補數概念，變出一堆1

# LeetCode 3370. Smallest Number With All Set Bits
# 從 n 開始往上找, 找到到「2進位表示時, 全部都是1」的數
class Solution:
    def smallestNumber(self, n: int) -> int:
        L = 0  # 想知道 n 在「二進位」裡，是「幾位數」
        while n>0:  # 利用「剝皮法」
            n = n // 2  # 把 n 以「二進位」風格剝皮
            L += 1  # 「二進位」的長度 + 1
        # 現在知道「二進位」的長度 L，以此為主，用迴圈「建出一堆1」
        ans = 0
        for i in range(L):  # 進行 L 次的迴圈
            ans = ans * 2 + 1  # 逐步「組出」一堆1的數
        return ans

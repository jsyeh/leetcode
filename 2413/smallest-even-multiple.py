# LeetCode 2413. Smallest Even Multiple
# 找出 2 和 n 的最小的倍數
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0: return n  # 如果是偶數，本身就是答案
        else: return n * 2  # 不然就剩2倍，就是答案

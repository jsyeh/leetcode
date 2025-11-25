# LeetCode 1015. Smallest Integer Divisible by K
# 給你 k，請你從 1 出發，找到第1個「數字只有1」的n，n%k==0
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Hint 只要持續取 k 的餘數
        # Hint 永遠無法整除的，是2和5的倍數
        if k%2==0 or k%5==0: return -1

        now = 1  # now 是取 k 的餘數的結果
        ans = 1  # ans 是目前累積「一堆1」的數的長度
        while now % k != 0:
            now = (now * 10 + 1) % k
            ans += 1

        return ans

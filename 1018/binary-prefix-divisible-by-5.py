# LeetCode 1018. Binary Prefix Divisible By 5
# nums 裡有一堆 0 和 1，以它為 prefix 的數，是5的倍數嗎？
# 因 nums 有 10^5 個 bit，所以要取 %5 才不會爆掉
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        now = 0
        for num in nums:
            now = (now * 2 + num)%5  # 逐步把 bit 加進去，再 %5 才不會爆掉
            if now==0: ans.append(True)
            else: ans.append(False)
        return ans

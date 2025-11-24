# LeetCode 1018. Binary Prefix Divisible By 5
# nums 裡有一堆 0 和 1，以它為 prefix 的數，是5的倍數嗎？
# 因 nums 最多有 10^5 個 bit，所以要取 % 5 才不會爆掉
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []  # 每個數 nums[i] 對應 ans[i]
        now = 0  # 累加的結果（會取5的餘數）
        for num in nums:  # 逐個數處理 nums[0]...nums[i]
            now = (now * 2 + num) % 5  # 把 bit 加入（再 % 5 才不會爆掉）
            if now==0: ans.append(True)  # 太好了，是5的倍數
            else: ans.append(False)  # 糟糕，不是5的倍數
        return ans

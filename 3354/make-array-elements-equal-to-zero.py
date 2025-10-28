# LeetCode 3354. Make Array Elements Equal to Zero
# 挑0當「開始位置」、決定左右的「開始方向」。遇0繼續走，遇>0「減1」再反彈。
# 從0開始，往左右持續「撞出一堆0」想「全部變成0」，問有幾種可能。
# 發現規則：找到每個0，「左邊和==右邊和」就有2種可能，「差1」就有1種可能
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)  # 全部總和，將拆一半
        preSum = 0
        ans = 0  # 總共有幾種可能
        for num in nums:  # 逐一檢查數字
            preSum += num  # 從左到右「加總」
            if num==0:  # 遇到0，是否能當「開始位置」呢？
                if preSum*2==total: ans += 2  # 往左右2，有2種可能
                if preSum*2==total-1: ans += 1  # 往左，有1種可能
                if preSum*2==total+1: ans += 1  # 往右，有1種可能
        return ans

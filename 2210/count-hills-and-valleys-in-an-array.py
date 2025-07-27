# LeetCode 2210. Count Hills and Valleys in an Array
# nums 陣列裡，找「有幾個山（最近的點是低）、谷（最近的點是高）」
# 題目英文要花點時間讀懂。
# Hill: 最近的不同高度是smaller, Valley: 最近的不同高度是 larger
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N = len(nums)  # nums 的數量
        state = 0  # 0: 一開始 1: 往上  -1: 往下
        change = 0  # 往上、往下的「改變次數」 # 山、谷 的數量
        for i in range(1, N):  # 相鄰的 nums[i-1] vs. nums[i] 比較
            if nums[i-1] < nums[i] and state != +1:  # 方向不同
                state = +1
                change += 1
            if nums[i-1] > nums[i] and state != -1:  # 方向不同
                state = -1
                change += 1
        if change <= 1: return 0  # 不足以構成任何山谷
        return change - 1  # 上上下下的改變次數 -1 會變成「山、谷」的個數

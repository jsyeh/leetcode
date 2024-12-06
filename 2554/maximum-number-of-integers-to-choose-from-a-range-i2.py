# LeetCode 2554. Maximum Number of Integers to Choose From a Range I
# 挑 1...n 之間的數，加起來要最大，但有些數 banned 不能用。
# 先把 banned 變成 set() 方便快速查表，再用 for 迴圈「小到大」挑數字
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)  # 先變成 set()，之後查詢速度會很快
        ans = 0  # 目前挑了幾個數
        nowSum = 0 # 由小到大，現在加總的結果
        for i in range(1, n+1):  # 在 1...n 之間挑數字
            if i not in banned:  # 若數字可以挑
                if nowSum + i > maxSum: break # 若太大，就結束
                nowSum += i  # 沒事，把數字加進去
                ans += 1  # 同時，答案 +1
        return ans

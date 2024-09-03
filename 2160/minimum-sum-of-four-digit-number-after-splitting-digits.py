# LeetCode 2160. Minimum Sum of Four Digit Number After Splitting Digits
# 有4位數1000-9999，將數字拆開、組成成2個數，問加起來「最小的數」
class Solution:
    def minimumSum(self, num: int) -> int:
        d = sorted(str(num))  # d 是 digits，把每位數，變成「小到大」的字串
        d = list(map(int, d))  # 「每位數」再轉成整數
        return d[0]*10 + d[1]*10 + d[2] + d[3]
        # 直覺：小的放十位數、大的放個位數

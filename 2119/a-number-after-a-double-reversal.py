# LeetCode 2119. A Number After a Double Reversal
# 把 2021 變 1202 再變回 2021 可以
# 把 12300 變成 321 再變回 123 不可以
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num%10 == 0 and num != 0: # 簡單的說，只要個位數是 0
            return False  # 就會轉換失敗 （除了 num==0 沒問題）
        return True

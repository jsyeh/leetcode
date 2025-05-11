# LeetCode 1550. Three Consecutive Odds 連續3個奇數
# 找找看 arr 裡，是不是有連續3個奇數
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for now in arr:
            if now%2==1: odd += 1
            else: odd = 0
            if odd>=3: return True
        return False

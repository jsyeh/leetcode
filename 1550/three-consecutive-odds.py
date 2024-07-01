# LeetCode 1550. Three Consecutive Odds 連續3個奇數
# 找找看 arr 裡，是不是有連續3個奇數
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0 # 一開始，有看到「連續0個奇數」
        for now in arr:
            if now%2==1:
                odd += 1  # 又找到1個奇數
                if odd>=3: return True  # 累積夠多個奇數
            else: # 如果現在是偶數
                odd = 0 # 就中斷「連續奇數」的個數，從0開始
        return False

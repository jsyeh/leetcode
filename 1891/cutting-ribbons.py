# LeetCode 1891. Cutting Ribbons
# ribbons[i] 是第 i 條 ribbon緞帶 的長度，
# 最少要剪出 k 條長度一樣的 ribbon緞帶，問 ribbon 長度最長能多長？
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def helper(maxLen):  # 反過來問，如果長度最長 maxLen 能剪出幾條
            ans = 0
            for ribbon in ribbons:
                ans += ribbon // maxLen  # 這條，可剪出「這麼多條」
            return ans
        left, right = 1, max(ribbons) + 1  # 最極端的2種長度
        while left < right:
            mid = (left+right) // 2
            if helper(mid) < k: # 「失敗」數目不夠，要再限縮長度
                right = mid
            else:  # 數目足夠，可「再挑戰大」一點、長一點，直到「失敗」為止
                left = mid + 1
        # left 將是「剛好不行」的長度，所以 left - 1 就是答案
        return left - 1

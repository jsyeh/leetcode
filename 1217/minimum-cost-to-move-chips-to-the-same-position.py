# LeetCode 1217. Minimum Cost to Move Chips to The Same Position
# 移動「偶數步」不用cost，移動1步要cost=1，把全部 chips 籌碼移到同一格，要多少 cost?
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 因為移動「偶數步」不用cost，所以所有的偶數可放一堆、奇數也能放一堆
        odd, even = 0, 0  # 分成「奇數堆、偶數堆」
        for p in position:
            if p%2==0: even += 1
            else: odd += 1
        # 比較小堆的，是答案，因為它們要移到「另一堆」大堆的。
        if odd<even: return odd
        else: return even

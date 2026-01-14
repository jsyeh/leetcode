# LeetCode 875. Koko Eating Bananas
# Koko 要決定「吃香蕉的速度k」，才能在 h 小時內，吃掉 piles 裡全部的香蕉
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 可用 binary search，找到最小的 k
        def helper(k):  # 請問「吃香蕉的速度k」能否在h小時內完成任務
            t = 0
            for pile in piles:  # 針對「每堆」的數量，進行分析
                t += ceil(pile/k)  # 要 ceil(pile/k) 次，才能吃完
            return t <= h  # 能成功嗎？
        # for i in range(1,max(piles)+1): 
        #    print(helper(i), end=' ')  # 印出來，觀察插入的位置在哪裡
        # k 需為 1-index (分母不為 0) 但 bisect_left() 是 0-index 所以要加 1
        return bisect_left(range(1,max(piles)+1), True, key=helper) + 1


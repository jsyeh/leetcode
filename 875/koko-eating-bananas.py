class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatInTime(t) -> bool:
            # 先用 binary search 找到t以下的值
            # 或用暴力法去找也行
            hours = 0 # 使用的時間
            for p in piles:
                if p<=t: hours += 1
                else:
                    hours += p // t
                    if p%t>0: hours += 1
            if hours<=h: return True
            else: return False
        
        piles.sort()
        N = len(piles)
        left, right = 1, piles[N-1]
        while left<right:
            mid = (left+right) // 2
            if canEatInTime(mid):
                right = mid # 夠快，所以可以再吃更快
            else:
                left = mid + 1
        return left
# case 18/125: [312884470] 968709470

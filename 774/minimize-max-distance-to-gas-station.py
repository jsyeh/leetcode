# LeetCode 774. Minimize Max Distance to Gas Station
# stations 加油站位置（在x軸的一直線），你要再增加 k 個加油站
# 希望「相鄰加油站的距離」最大值「最小」，找出這個值。
# 因 k 很大，不能用 heap 來模擬。可把 2000 個數的間隔，用數學分析
# 可用 binary search 找答案
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        gap = [stations[i] - stations[i-1] for i in range(1,len(stations))]
        def helper(ans):
            k2 = 0  # 需增加 k2 個加油站，才能讓答案為 ans
            for g in gap:
                if g > ans: k2 += ceil(g/ans) - 1
            return k2 <= k  # 能否用 k 個加油站「達成任務」
        left, right = 0, max(gap)
        while left < right:  # 利用 binary search 來逼近答案
            mid = (left+right) / 2  # 浮點數
            if helper(mid):  # 成立，代表答案可以更小
                right = mid - 0.000001
            else:  # 不成立，代表答案要再大一點
                left = mid + 0.000001
        return right

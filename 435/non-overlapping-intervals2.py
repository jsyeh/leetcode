# LeetCode 435. Non-overlapping Intervals
# 刪掉最少的 intervals 讓其他都不會有重疊
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prevStart, prevEnd = -inf, -inf
        ans = 0
        for start, end in intervals:
            if prevEnd <= start:  # 沒有重疊
                prevStart, prevEnd = start, end
            else:  # 有重疊
                ans += 1  # 遇到一組重疊，需要刪
        
        return ans

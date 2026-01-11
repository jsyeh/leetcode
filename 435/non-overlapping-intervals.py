# LeetCode 435. Non-overlapping Intervals
# 刪掉最少的 intervals 讓其他都不會有重疊
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])  # 以結束時間排序、處理
        # 重疊時，就一定要刪。刪「卡到最多人」的那個
        totalEnd = -inf
        ans = 0
        for nowStart, nowEnd in intervals:
            if nowStart < totalEnd:  # 時間重疊
                ans += 1  # 要刪掉這個
            else:  # 因已 sort，nowEnd 會慢慢往右
                totalEnd = nowEnd
        return ans

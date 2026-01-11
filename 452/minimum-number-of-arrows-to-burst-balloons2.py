# LeetCode 452. Minimum Number of Arrows to Burst Balloons
# 氣球超寬的，從[start,end]中間射過的箭，都能把這個氣球弄破
# 要多少箭，才能把「全部的氣球」都弄破。
# 策略：以「氣球end的位置」排序，再依序處理
# 挑個氣球，射它的最end的位置，後面的氣球，只要start還在左邊，就還在「一箭」的範圍
# 如果 start 跑到前一個的end的右邊，那就無法「一箭搞定」只好再加「新箭」
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans = 0
        prevEnd = -inf
        for start, end in points:
            if prevEnd < start:
                prevEnd = end
                ans += 1
        return ans

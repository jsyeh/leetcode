# 氣球超寬的，從[start,end]中間射過的箭，都能把這個氣球弄破
# 要多少箭，才能把「全部的氣球」都弄破。
# 策略：以「氣球end的位置」排序，再依序處理
# 挑個氣球，射它的最end的位置，後面的氣球，只要start還在左邊，就還在「一箭」的範圍
# 如果 start 跑到前一個的end的右邊，那就無法「一箭搞定」只好再加「新箭」
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]) # 以 右邊界 x_end 排序
        ans = 1 # 因最少有1個氣球，所以最少有1箭，放在end的位置（發射）
        end = points[0][1] # 前一箭射的位置
        for x_start, x_end in points:
            if end < x_start: # 範圍外, 需要新的一箭
                ans += 1 # 加一箭
                end = x_end # 這個難搞的氣球，右邊界當成我們要射箭的地方
        return ans

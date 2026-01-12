# LeetCode 1266. Minimum Time Visiting All Points
# 這題超簡單：照順序，走過每個點。直走、橫走、斜走1格都1秒，要花多少時間?
# 直接 for 迴圈，配合 max(dx,dy) 加起來便是答案
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        x, y = zip(*points)  # 用 zip() 的 zip(*points)拆成一堆x、一堆y
        for i in range(1,len(points)):
            ans += max(abs(x[i]-x[i-1]), abs(y[i]-y[i-1]))
        return ans

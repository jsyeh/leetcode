# points在同一條線嗎？ 3點都沒共線，叫 boomerang迴旋鏢的路徑
# 總共就3個點，直接暴力做就行了
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dx = points[1][0] - points[0][0]
        dy = points[1][1] - points[0][1]
        dx2 = points[2][0] - points[0][0]
        dy2 = points[2][1] - points[0][1]
        # 利用交叉相乘的概念即可
        if dx*dy2==dy*dx2: return False
        else: return True

# LeetCode 3516. Find Closest Person
# 給直線上 x y z 三個人的座標，其中 x 和 y 會往 z 移動，誰會先到？
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) < abs(y-z): return 1  # 在座標 x 的人先到
        if abs(y-z) < abs(x-z): return 2  # 在座標 y 的人先到
        return 0  # 兩個人一起到達座標z

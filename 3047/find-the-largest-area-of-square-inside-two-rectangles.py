# LeetCode 3047. Find the Largest Area of Square Inside Two Rectangles
# bottomLeft[i] 和 topRight[i] 構成長方形，找「2個長方形裡」最大的正方形
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        N = len(bottomLeft)
        ans = 0  # 最大的正方形的「邊長」
        # 利用排列組合，把 四邊形p 和 四邊形q 全部試迥一次
        for (p0,p1),(q0,q1) in combinations(zip(bottomLeft,topRight),2):
            dx = min(p1[0],q1[0]) - max(p0[0],q0[0])  # x 方向「範圍」交集部分
            dy = min(p1[1],q1[1]) - max(p0[1],q0[1])  # y 方向「範圍」交集部分
            if dx<=0 or dy<=0: continue  # 有負的，代表「沒有交集」
            ans = max(ans, min(dx,dy))  # 「更新」最大的正方形的「邊長」
        return ans * ans  # 對應的面積

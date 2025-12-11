# LeetCode 3531. Count Covered Buildings
# n x n 地圖中，建築 buildings[i] 座標 x,y 
# 若地圖的「左右上下」都至少有1個建築，叫covered，問總共有幾個 covered 建築
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        top = [-1] * (n+1)  # 四個方向，都建立「對照表」
        down = [inf] * (n+1)  # 因 1 <= x,y <=n 所以設 -1 和 inf 當預設值
        left = [inf] * (n+1)
        right = [-1] * (n+1)
        for x,y in buildings:  # 先用迴圈，逐一更新「對照表」
            top[x] = max(top[x], y)
            down[x] = min(down[x], y)
            left[y] = min(left[y], x)
            right[y] = max(right[y], x)
        ans = 0
        for x,y in buildings:  # 再用迴圈，逐一檢查是否在「對照表」的範圍內
            if top[x]>y and down[x]<y and left[y]<x and right[y]>x:
                ans += 1
        return ans

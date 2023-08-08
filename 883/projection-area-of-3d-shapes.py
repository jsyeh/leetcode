# 想要計算「三視圖」裡，每個平面的面積，要加起來
# 其實有點像是 row 的最大值、col的最大值等
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        area1, area2, area3 = 0, 0, 0
        rows = [0]*M
        cols = [0]*N
        for i in range(M):
            for j in range(N):
                v = grid[i][j]
                if v > 0:
                    area1 += 1 # 上視圖
                    if v > rows[i]: rows[i] = v # 找 rows[i] 最高值
                    if v > cols[j]: cols[j] = v # 找 cols[j] 最高值
        
        for i in range(M):
            area2 += rows[i] # 描面積
        for j in range(N):
            area3 += cols[j] # 描面積
        return area1 + area2 + area3

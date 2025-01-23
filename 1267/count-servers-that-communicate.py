# LeetCode 1267. Count Servers that Communicate
# 地圖 grid[i][j] 裡 1:有電腦，0:沒有電腦，兩台電腦在同一直線or橫線「可互連」。
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        rows, cols = [0]*M, [0]*N
        computer = 0  # 問「有幾台電腦」可連到其他台電腦？
        for i in range(M):  # 先統計電腦在哪裡
            for j in range(N):
                if grid[i][j]==1:
                    rows[i] += 1  # 第 i row 多1台電腦
                    cols[j] += 1  # 第 j row 多1台電腦
                    computer += 1  # 電腦的總數
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1 and rows[i]==1 and cols[j]==1:
                    computer -= 1  # 遇到落單的電腦，扣掉它
        return computer  # 最後留著的電腦，都有同伴「可互連」

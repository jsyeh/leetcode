# LeetCode 2257. Count Unguarded Cells in the Grid
# 在 m x n 的格子裡，有 guards 可往「前後左右」看，但 walls 會擋住視線
# 問「有幾個格子」沒辦法被 guards 看到？
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cell = [[0]*n for i in range(m)]  # 建出全部格子
        for i,j in guards + walls:  # 警衛及牆，都會擋住視線，標注起來
            cell[i][j] = 1  # 0還沒走過，1警衛或牆擋住
        for i2,j2 in guards:  # 每個警衛，逐一巡4個方向
            for di,dj in (1,0),(-1,0),(0,1),(0,-1):  # 4個方向、前進方向
                i, j = i2, j2  # 回到警衛的起始位置
                while True:  # 沒超過邊界
                    i, j = i+di, j+dj  # 前進1格
                    if i<0 or i>=m or j<0 or j>=n: break # 超過邊界
                    if cell[i][j]==1: break  # 擋住，別再走
                    cell[i][j] = 2  # 可巡視到、視線不會被擋到、看得到的格子
        return sum(row.count(0) for row in cell)  # 數「最後剩幾個0」沒被看到

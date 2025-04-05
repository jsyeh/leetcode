# LeetCode 317. Shortest Distance from All Buildings
# m x n grid 裡 0 代表空白，1代表建築，2代表阻礙，只有 0 能上下左右走
# 找離其他建築的總距離最小的「空白格子」建房子，距離 -1 代表無法找到
# 題目與 296. Best Meeting Point 很接近
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        counter = Counter(grid[i][j] for i in range(M) for j in range(N))  # 計算「幾個0、幾個1」
        if counter[0]==0: return -1  # 沒地方建房子，直接失敗
        totalBuilding = counter[1]
        distSum = [[0]*N for i in range(M)]  # 累積 grid[i][j] 到每個建築的距離
        hitBuilding = [[0]*N for i in range(M)]  # 從 grid[i][j] 出發，能到達幾個建築

        def bfs(startI, startJ):  # 從某個建築的座標出發，累積 distSum
            queue = deque()
            visited = set()
            queue.append((0,startI,startJ))  # 距離、座標
            visited.add((startI,startJ))
            building = 1  # 從某個建築物出發
            while queue:
                d, i, j = queue.popleft()
                for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 避開邊界
                    if (ii,jj) in visited: continue  # 避開走過的地方
                    visited.add((ii,jj))
                    if grid[ii][jj]==0:  # 從建築 (i,j) 到 空格 (ii,jj)
                        distSum[ii][jj] += d + 1  # 的最矩距離是 d+1，要累積全部的建築哦
                        hitBuilding[ii][jj] += 1  # 此格可到的建築數+1
                        queue.append((d+1,ii,jj))  # 把新的位置，加到 queue 裡
                    elif grid[ii][jj]==1: building += 1  # 能到的建築數+1
            return building  # 這次 bfs() 更新、收集到「幾個空格」
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:  # 從建築 i,j 出發
                    building = bfs(i,j)  # 這次有「每個空格」有更新到距離（累積到distSum陣列裡）
                    if building != counter[1]: return -1  # 若沒更新到「全部建築」，就失敗 -1
        allPosition = [distSum[i][j] for i in range(M) for j in range(N) if grid[i][j]==0 and hitBuilding[i][j]==counter[1]]  # 每個空格的「累積距離」
        if allPosition==[]: return -1  # 沒有任何空格「能走達全部建築」就 return -1
        return min(allPosition)  # 看哪個空格「累積距離」最小（二維陣列，已經成一維陣列，並去除其他值，可用 min() 

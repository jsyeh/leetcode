# LeetCode 1730. Shortest Path to Get Food
# grid 裡 * 是你的位置，# 是食物，X 會卡住，能走 O，最快吃到食物
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # 使用 BFS 就可找到答案
        queue = deque()  # BFS 的 queue 資料結構
        visited = set()  # 走過的格子

        M, N = len(grid), len(grid[0])  # 長寬
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='*':
                    queue.append((0, i, j))  # 起點，0步
                    visited.add((i,j))  # 標示走過
        
        while queue:  # 還能 BFS 的話
            step, i, j = queue.popleft()  # 現在在哪裡
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: 
                    continue # 超過邊界，避開
                if grid[ii][jj]=='#':  # 找到食物，太好了
                    return step + 1  # 到食物「要走幾步」
                if grid[ii][jj]=='X' or (ii,jj) in visited:
                    continue  # 不能走 or 走過，避開
                queue.append((step+1, ii, jj))
                visited.add((ii,jj))
        return -1  # 找不到食物

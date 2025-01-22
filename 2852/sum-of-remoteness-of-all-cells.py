# LeetCode 2852. Sum of Remoteness of All Cells
# R[i][j] 是把遠離的「格子」加起來。要把 R[i][j] 全部加起來
# 等價於： total * totalCount, 再把每群「相連格子的和」*「相連格子數量」減掉
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # 長、寬
        total = 0  # grid[i][j] 裡，non-blocked 的值全部加起來
        totalCount = 0  # non-blocked 的格子「有幾個」
        ans = 0  # 最後的答案 = total * totalCount 再減掉「每群的和」*「對應格子數」
        for i in range(M):
            for j in range(N):
                if grid[i][j] == -1: continue  # 避開 blocked 的格子
                total += grid[i][j]  # 更新 non-blocked 的總和
                totalCount += 1  # 更新 non-blocked 的格子數量
                now = grid[i][j]  # 現在這塊的 sum 是多少（先有自己這格的值）
                count = 1  # 現在這塊有幾個格子（先有自己的這格）
                grid[i][j] = -1  # 走過，標示不要再走
                queue = deque()  # 利用 queue 進行 BFS
                queue.append((i,j))
                while queue:
                    i0, j0 = queue.popleft()
                    for ii,jj in (i0+1,j0),(i0-1,j0),(i0,j0+1),(i0,j0-1):  # 四方向的鄰居
                        if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 超過邊界
                        if grid[ii][jj]==-1: continue  # blocked 或「走過」
                        total += grid[ii][jj]
                        totalCount += 1
                        now += grid[ii][jj]
                        count += 1
                        grid[ii][jj] = -1  # 標示 blocked 代表「走過」就不要再走
                        queue.append((ii,jj))  # 加入 queue 以便
                ans -= now * count  # 要減掉「這群的和」*「這群的數量」
        ans += total * totalCount  # 最後（有了準確的total及totalCount後）再補加「全部」的部分
        return ans

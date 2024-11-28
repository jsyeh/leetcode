# LeetCode 2290. Minimum Obstacle Removal to Reach Corner
# 想從「左上角」走到「右下角」，但路上很多「阻擋物」，問「最少移走幾個」便能有道路能走
# 如果只能「往右、往下」那「動態規劃」可解。但現在能「上下左右」4個方向，就有難度
# 以下程式，模仿 Solution 裡 rock 的 Method 2 modified BFS 短而有力。
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dist = [[inf]*N for _ in range(M)]  # 還沒走到的格子，距離先設inf無限大
        dist[0][0] = 0  # 從左上角出發
        queue = deque()  # 左邊塞cost同等級的stack，右邊塞cost+1的queue
        queue.append((0,(0,0)))  # 從 (0,0) 出發，cost是0
        while queue:  # BFS 持續做
            cost, (i,j) = queue.popleft()
            for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 上下右左4個方向
                if 0<=ii<M and 0<=jj<N and dist[ii][jj]==inf:  # 範圍內沒走過的目標
                    if grid[ii][jj]==1:  # 目標若是1，是阻擋物
                        dist[ii][jj] = cost + 1  # 要到的cost變+1
                        queue.append((cost+1, (ii,jj)))  # 再丟進queue 遠的
                    else:  # 目標是0，空的
                        dist[ii][jj] = cost  # cost不變
                        queue.appendleft((cost, (ii,jj)))  # 同一國的（有點像stack一起處理）
        return dist[M-1][N-1]  # 最「右下角」的距離

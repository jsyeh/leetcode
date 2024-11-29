# LeetCode 2577. Minimum Time to Visit a Cell In a Grid
# 你要參觀的格子，需「準備好」的時間 grid[i][j] 才能進入。從左上角(0,0)出發，每移1格要1秒。
# 能順利走到「右下角」嗎？最快何時能到？對了！為拖時間，可重覆在附近格子「閒逛」，直到某個格子「解鎖」開放哦！
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = set()  # 標記「走過」的格子
        visited.add((0,0))  # 「走過」出發點的格子
        heap = []  # 使用 priority queue (heap) 進行 BFS
        heappush(heap, (0,0,0))  # 出發點。time:0 在座標 (0,0)
        while heap:  # 使用 priority queue 進行 BFS
            t, i, j = heappop(heap)  # 時間 t 時，在 (i,j)
            canDelay = False
            for ii,jj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):  # 上下左右4方向
                if 0<=ii<M and 0<=jj<N and ((ii,jj) in visited or t+1>=grid[ii][jj]):
                    canDelay = True  # 附近有格子可「閒逛」，很好！
            for ii,jj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):  # 上下左右4方向
                if 0<=ii<M and 0<=jj<N: # 再一次檢查四周
                    if (ii,jj) not in visited and t+1>=grid[ii][jj]: # 此時間可進入
                        if ii==M-1 and jj==N-1: return t+1  # 到達終點
                        heappush(heap, (t+1, ii, jj))
                        visited.add((ii,jj))
                    elif (ii,jj) not in visited and canDelay:  # 時間還沒到，但可附近「閒逛」等到時間到
                        diff = (grid[ii][jj]-t)//2*2
                        if ii==M-1 and jj==N-1: return t+1+diff  # 到達終點
                        heappush(heap, (t+1+diff, ii, jj))
                        visited.add((ii,jj))
        return -1  # 走不到

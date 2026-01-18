# LeetCode 505. The Maze II
# 迷宮裡，可往上下左右踢球，球撞到牆後會停下來。問走幾格後，到達「終點」
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        M, N = len(maze), len(maze[0])  # 長、寬
        dist = [[inf]*N for i in range(M)]  # 看 step 是否更短
        dist[start[0]][start[1]] = 0  # 起點的 step 是 0
        heap = [(0,start)]  # 用 heap 先處理 step 小的座標
        while heap:  # 只要還有 heap
            step0, (i0,j0) = heappop(heap)  # step 最小的座標
            if [i0,j0]==destination: return step0  # 到達「終點」
            if step0 > dist[i0][j0]: continue  # 已是舊的走法，不行
            for di,dj in (-1,0),(1,0),(0,-1),(0,1):  # 上下左右踢球
                i, j, step = i0, j0, step0  # 這次的起點
                while 0<=i+di<M and 0<=j+dj<N and maze[i+di][j+dj]==0:
                    i, j, step = i+di, j+dj, step+1  # 沒撞到牆，繼續滾
                if dist[i][j]<=step: continue  # 撞到牆停下，不夠好、不行
                dist[i][j] = step  # 更好的距離，更新
                heappush(heap, (step, (i,j)) )  # 放入 heap
        return -1

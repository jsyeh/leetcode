class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        dist = [[inf]*N for _ in range(M)]

        dd = [[0,1], [0,-1], [1,0], [-1,0]] # 四個移動的方向

        heap = []
        heappush(heap, [0, start[0], start[1]]) # distance, x, y
        while len(heap)>0:
            d0, x0, y0 = heappop(heap) # distance, x, y
            for dx,dy in dd: # 往4個方向依序走走
                d, x, y = d0, x0, y0 # 因為值會改，所以從備份的d0,x0,y0拿來用
                while x+dx>=0 and y+dy>=0 and x+dx<M and y+dy<N and maze[x+dx][y+dy]==0:
                    # 只要還能走，就繼續走到底
                    d, x, y = d+1, x+dx, y+dy

                # （撞牆）停下來時，看是不是到達目的地
                if x==destination[0] and y == destination[1]:
                    return d
                # 如果值更好的話，更新dist，並丟到heap裡
                if d<dist[x][y]:
                    dist[x][y] = d
                    heappush(heap, [d, x, y])
                
        return -1 # 都沒到達目標，就-1失敗

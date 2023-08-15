# 看題目，很像倉庫番的移動方式
# 到過的位置可放入 hashset 裡，表示 visited
# 移動時，用BFS/queue來解決，4個方向的移動
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        M = len(maze)
        N = len(maze[0])
        visited = set()
        queue = deque() # append(), popleft() 便能當成 queue
        # 平常要記得先 from collections import deque 才能用 deque()

        queue.append(start)
        def toString(pos: List[int])->str: # 把座標變成字串
            return str(pos[0]) + "," + str(pos[1])
        visited.add(toString(start)) # 把座標變成字串，方便hash記錄

        def go(dx:int, dy:int, pos:List[int])->List[int]:
            x, y = pos # 把座標當成 x, y （因 row,col對應 y, x 不好理解）
            while x+dx >=0 and y+dy >=0 and x+dx <M and y+dy<N and maze[x+dx][y+dy]==0:
                # 照位移量，移到撞牆前
                x += dx
                y += dy
            return [x, y]
        while len(queue)>0:
            pos = queue.popleft()
            dx = [0,1,0,-1] # 建立4個方向的位移量
            dy = [1,0,-1,0] # 建立4個方向的位移量
            for dir in range(4):
                next = go(dx[dir], dy[dir], pos) # 照位移量，移到撞牆前
                if next == destination: return True # 很好，提早到達終點
                if toString(next) not in visited: # 如果沒走過這裡
                    queue.append(next) # 加入 queue
                    visited.add(toString(next)) # 並記錄這裡走過了
        return False # 無法走到/queue用完了，就失敗了


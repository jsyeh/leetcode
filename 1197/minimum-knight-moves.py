# 看來像動態規劃的題目，依序查看每個「格子」要「幾步」能到
# 可 配合 queue=deque() 使用 BFS 來走棋子
# 運氣很好，Python 的 list index可以是負的，方便程式更簡潔
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x==0 and y==0: return 0 # 漏了這個初始值

        visited = [[False]*610 for _ in range(610)]
        queue = deque() # DFS
        queue.append([0,0,0]) # x, y, steps
        visited[0][0] = True # 出發點，是第0步

        dx = [2, 1,-1,-2,-2,-1, 1, 2] # 8個方向
        dy = [1, 2, 2, 1,-1,-2,-2,-1]

        while len(queue)>0:
            x1, y1, step = queue.popleft()
            for i in range(8):
                x2, y2 = x1+dx[i], y1+dy[i]
                if x2==x and y2==y:
                    return step+1 # 走到了
                if visited[x2][y2]==False:
                    queue.append([x2,y2,step+1])
                    visited[x2][y2]=True # 要標示，以免重覆走
                    # 不然「1進8出」成長太快 queue爆炸
                    # 會 Memory Limit Exceeded 
        return 0
# case 44/45: 0, 0

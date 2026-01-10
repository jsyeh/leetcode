# LeetCode 1926. Nearest Exit from Entrance in Maze
# maze 陣列裡 '.' 是可走的格子。從 entrance 出發，要走幾步，能離開迷宮
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        i,j = entrance
        # 入口 != 出口，所以下一行不能用
        # if i==0 or j==0 or i>=M-1 or j>=N-1: return 0  # 直接在出口

        queue = deque()
        queue.append( (0, i, j) )

        visited = set( [(i,j)] )
        while queue:
            step, i, j = queue.popleft()
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii==entrance[0] and jj==entrance[1]: continue  # 避開入口
                if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 避開出界
                if maze[ii][jj]=='+': continue
                if ii==0 or jj==0 or ii==M-1 or jj==N-1: return step+1
                if (ii,jj) in visited: continue
                visited.add( (ii,jj) )
                queue.append( (step+1,ii,jj) )
        return -1

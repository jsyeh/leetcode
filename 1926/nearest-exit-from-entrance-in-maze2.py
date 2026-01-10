# LeetCode 1926. Nearest Exit from Entrance in Maze
# maze 陣列裡 '.' 是可走的格子。從 entrance 出發，要走幾步，能離開迷宮
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance,0))
        visited = set()
        visited.add(tuple(entrance))
        while queue:
            (i,j),step = queue.popleft()
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: continue
                if (ii,jj) in visited or maze[ii][jj]=='+': continue
                if ii==0 or jj==0 or ii==M-1 or jj==N-1: return step+1
                queue.append(((ii,jj),step+1))
                visited.add((ii,jj))
        return -1

# LeetCode 490. The Maze
# 很像倉庫番，球每次滾動「撞到牆」會停止。問能否停在「終點」
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        M, N = len(maze), len(maze[0])
        queue = deque()
        queue.append(start)  # 從 start 出發
        visited = set([tuple(start)])  # 標註「走過」
        while queue:
            i0,j0 = queue.popleft()
            for di,dj in (1,0),(-1,0),(0,1),(0,-1):
                i,j = i0,j0
                while 0<=i+di<M and 0<=j+dj<N:
                    if maze[i+di][j+dj]==0:  # 能走
                        i,j = i+di,j+dj  # 就走
                    else: break  # 撞到牆，就離開
                if [i,j]==destination:  # 到達終點
                    return True  # 成功
                if (i,j) not in visited:
                    queue.append((i,j))  # 新的出發點
                    visited.add((i,j))  # 標註「走過」
        return False  # 沒有成功，就是失敗

# LeetCode 994. Rotting Oranges
# 橘子會依序爛掉
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        fresh = 0  # 數一數，有幾個新鮮的橘子
        queue = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j]==2:  # 爛掉的橘子
                    queue.append( [0,i,j] )  # 加入 queue 進行 BFS
                elif grid[i][j]==1:  # 新鮮的橘子
                    fresh += 1
        if fresh==0:  # 沒剩任何新鮮的橘子
            return 0  # 任務就結束了！
        while queue:
            t, i, j = queue.popleft()
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: continue
                if grid[ii][jj]==1:  # 新鮮的橘子，將會爛掉
                    grid[ii][jj] = 2  # 爛掉囉
                    fresh -= 1  # 少一顆新鮮的橘子
                    if fresh==0:  # 沒有新鮮的橘子了
                        return t+1  # 它是在 t+1 的時候爛掉
                    queue.append( [t+1,ii,jj] )
        return -1  # 沒全部爛掉，失敗

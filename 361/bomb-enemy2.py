# LeetCode 361. Bomb Enemy
# m x n 的 grid 裡，grid[i][j] 可能是 'W':牆、'E':敵人、'0':空格
# 挑1格「放炸彈」，會往「上下左右」4方向炸，遇到牆就停住。最多炸幾個人？
# 可「左到右」「右到左」「上到下」「下到上」4個方向依序累積，再找最大即可
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        left = [[0] * N for i in range(M)]  # 左邊累積幾個
        right = [[0] * N for i in range(M)]  # 右邊累積幾個
        up = [[0] * N for i in range(M)]  # 上面累積幾個
        down = [[0] * N for i in range(M)]  # 下面累積幾個
        kill = [0] * 4  # 4個方向的累積變數
        for i in range(M):
            kill[0] = kill[1] = 0  # 左右2個方向
            for j in range(N):
                if grid[i][j]=='W': kill[0] = 0
                elif grid[i][j]=='E': kill[0] += 1
                left[i][j] = kill[0]
                if grid[i][N-1-j]=='W': kill[1] = 0
                elif grid[i][N-1-j]=='E': kill[1] += 1
                right[i][N-1-j] = kill[1]
        for j in range(N):
            kill[2] = kill[3] = 0  # 上下2個方向
            for i in range(M):
                if grid[i][j]=='W': kill[2] = 0
                elif grid[i][j]=='E': kill[2] += 1
                up[i][j] = kill[2]
                if grid[M-1-i][j]=='W': kill[3] = 0
                elif grid[M-1-i][j]=='E': kill[3] += 1
                down[M-1-i][j] = kill[3]
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='0':  # 空格才能放炸彈
                    ans = max(ans, left[i][j]+right[i][j]+up[i][j]+down[i][j])
        return ans

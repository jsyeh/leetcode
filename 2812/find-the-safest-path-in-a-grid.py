# 找到 grid[i][j] 裡, 最安全的一條路: grid[i][j]=1代表有小偷, grid[i][j]=0代表安全
# 你要離小偷「越遠越好」這時候問你, 你找到的那條「最安全的路」離小偷多遠?
# 一開始在 0,0 的位置出發, 到最右下角。若一開始就撞到小偷, 那就沒救了, 距離是0。
# 我想到的方法, 先是找到每一格的位置「離小偷的距離」。這可以使用 BFS 做到。
# 但是再來就麻煩了, 要怎麼找到一條(最安全回家的)路? 我覺得這題是 Hard 題
# 在 Editorial 裡, 有介紹 Binary Search 的技巧, 也就是「答案是d嗎?」
#  如果是, 那 dfs(0,0) 在走的時候, 會希望走的格子,是「危險
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        queue = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # 距離小偷0
                    queue.append((0, (i, j)))
                else:
                    grid[i][j] = -1  # 還沒有走過的格子

        def bfs(d, i, j):
            if i < 0 or j < 0 or i >= M or j >= N:
                return
            if grid[i][j] == -1:
                grid[i][j] = d
                queue.append((d, (i, j)))

        while len(queue) > 0:
            d, (i, j) = queue.popleft()
            bfs(d + 1, i + 1, j)
            bfs(d + 1, i - 1, j)
            bfs(d + 1, i, j + 1)
            bfs(d + 1, i, j - 1)

        def dfs(i, j, d):
            if i < 0 or j < 0 or i >= M or j >= N:
                return False  # 超過邊界，不能走
            if grid[i][j] < d or self.visited[i][j]:
                return False  # 離小偷太近，也不能走
            self.visited[i][j] = True
            if i == M - 1 and j == N - 1:
                self.visited[i][j] = False
                return True  # 順利到達右下角終點
            return dfs(i+1,j,d) or dfs(i,j+1,d) or dfs(i-1,j,d) or dfs(i,j-1,d)

        left, right = 0, M + N - 1
        while left < right:  # binary search, 看能走的距離是多少
            mid = (left + right) // 2
            self.visited = [[False] * N for _ in range(M)]
            if dfs(0, 0, mid):  # 如果能照著 mid 的距離條件走成功
                left = mid + 1
            else:  # 不能走
                right = mid
        return left - 1
# case 528/1036: [[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]]

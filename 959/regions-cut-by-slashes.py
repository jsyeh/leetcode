# 把 NxN 的方塊，在 grid[i][j] 裡用 ' ' '/' '\\' 切它
# 問「最會後會成幾片」
# 有點像 connected component 的題目，使用 BFS or DFS 應該就解掉了
# 但是NxN 會放大成 3N x 3N 的話，9宮格來裁
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        board = [[True]*3*N for _ in range(3*N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j]==' ': continue
                elif grid[i][j]=='/':
                    board[3*i+0][3*j+2] = False
                    board[3*i+1][3*j+1] = False
                    board[3*i+2][3*j+0] = False
                else: # \ 反斜線
                    board[3*i+0][3*j+0] = False
                    board[3*i+1][3*j+1] = False
                    board[3*i+2][3*j+2] = False
        # 建好大表格 board 後，可用 BFS or DFS 來找找
        def DFS(i, j):
            if i<0 or j<0 or i>=3*N or j>=3*N: return # 超過邊界
            if board[i][j]==False: return # 走過了
            board[i][j] = False # 標示走過，之後不能再走
            DFS(i+1,j)
            DFS(i-1,j)
            DFS(i,j+1)
            DFS(i,j-1)
        # 找找看有幾個獨立的 region
        ans = 0 # 有幾個獨立的 region
        for ii in range(3*N):
            for jj in range(3*N):
                if board[ii][jj]: # 是空的，就開始走
                    ans += 1 # 找到1個獨立的region
                    DFS(ii,jj) # 走過的地方，都會標示走過，以免重覆走
        return ans

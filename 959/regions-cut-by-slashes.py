# LeetCode 959. Regions Cut By Slashes
# NxN 的方塊，在 grid[i][j] 裡用 ' ' '/' '\\' 切它，問「最會後會成幾片」
# 把 NxN 放大成 3N x 3N，「9宮格」來裁，像 connected component，用 BFS or DFS 可解
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        board = [[True]*3*N for _ in range(3*N)] # 大表格，標示能走的區域
        for i in range(N): # 先利用2層迴圈，把「小表格」 變 「大表格」
            for j in range(N):
                if grid[i][j]=='/': # 右上往左下切，九宮格也照著斷開
                    board[3*i+0][3*j+2] = False
                    board[3*i+1][3*j+1] = False
                    board[3*i+2][3*j+0] = False
                elif grid[i][j]=='\\' # \ 反斜線 左上往右下切
                    board[3*i+0][3*j+0] = False
                    board[3*i+1][3*j+1] = False
                    board[3*i+2][3*j+2] = False
        def DFS(i, j):  # 建好大表格 board 後，可用 BFS or DFS 來找找
            if i<0 or j<0 or i>=3*N or j>=3*N or board[i][j]==False: return # 超過邊界or走過
            board[i][j] = False # 標示走過，之後不能再走
            DFS(i+1,j)
            DFS(i-1,j)
            DFS(i,j+1)
            DFS(i,j-1)
        ans = 0 # 找有幾個獨立的 region
        for ii in range(3*N):
            for jj in range(3*N):
                if board[ii][jj]: # 是空的，就開始走
                    ans += 1 # 找到1個獨立的region
                    DFS(ii,jj) # 走過的地方，都會標示走過，以免重覆走
        return ans

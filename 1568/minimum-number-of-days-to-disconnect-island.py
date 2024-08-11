# LeetCode 1568. Minimum Number of Days to Disconnect Island
# 在 grid[i][j] 有陸地1、海洋0，陸地上下左右相接。「要刪幾格陸地」才能斷開(不再1個島)
# 哇，原來有奇怪的秘密：Solutions GSAN 說 [you need at most 2 days]
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # 先算出長寬，以便迴圈使用
        def islands(grid,M,N):  # 算出「現在有幾個島」（有幾塊獨立的陸地）
            lands = 0  # 「島」一開始是0（每次呼叫islands()前，都要複製grid）
            for i in range(M):
                for j in range(N):
                    if grid[i][j]==1:  # 找到一格陸地
                        lands += 1  # 又多找到1個島，真好
                        DFS(grid,i,j,M,N)  # 用 函式呼叫函式 將相鄰的陸地都處理完
            return lands  # 總共找到的「島」
        def DFS(grid,i,j,M,N):  # 函式呼叫函式，DFS找出相鄰的陸地（並清掉）
            if i<0 or j<0 or i>=M or j>=N: return  # 超過邊界，不用再算
            if grid[i][j]==0: return  # 曾經走過，不用再算
            grid[i][j] = 0 # 清掉這格的陸地，以免「重覆走過」
            DFS(grid,i-1,j,M,N)  # 上，函式呼叫函式
            DFS(grid,i+1,j,M,N)  # 下，函式呼叫函式
            DFS(grid,i,j-1,M,N)  # 左，函式呼叫函式
            DFS(grid,i,j+1,M,N)  # 右，函式呼叫函式
        grid2 = [row[:] for row in grid]  # 複製 grid 到 grid2（呼叫islands()前，都要複製）
        if islands(grid2,M,N) != 1: return 0 # 合乎題目要求，不是1大塊，0天完成
        for i in range(M):  # 現在是一大塊，用迴圈「逐一」試試看，刪掉它，是否就「斷開/不再1個島」
            for j in range(N):
                if grid[i][j]==1: # 試著斷開
                    grid2 = [row[:] for row in grid]  # 複製 grid 到 grid2
                    grid2[i][j] = 0  # 將 [i][j] 這格刪掉
                    if lands(grid2,M,N) != 1: return 1  # 能切成功/不再是1個島
        return 2  # 前面1格（都）不成功，就要刪2格 [you need at most 2 days]

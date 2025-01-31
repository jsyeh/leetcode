# LeetCode 827. Making A Large Island
# n x n grid 可把 1 個 0 變 1，問能做出「最大片的1」 有多大。
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        label = [[-1]*N for _ in range(N)]  # 正方形標籤，將標注「大小」及「編號」（預設-1）
        def dfsArea(i,j):  # 「函式呼叫函式」算出面積
            if grid[i][j]==0: return 0
            area = 1
            grid[i][j] = -1  # 面積算過，標示為-1，之後就不會再算
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=ii<N and 0<=jj<N and grid[ii][jj]==1:
                    area += dfsArea(ii,jj)  # 「函式呼叫函式」算出面積
            return area
        def dfsLabel(i, j, area, pos): # 「函式呼叫函式」標示label[i][j]資訊
            if grid[i][j]==-1:
                label[i][j] = (area,pos)  # 標註「大小」及「編號」
                grid[i][j] = 1  # 之前 dfsArea()標成-1，現現再標示回1，還原回去
                for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=ii<N and 0<=jj<N and grid[ii][jj]==-1:
                        dfsLabel(ii,jj, area, pos) # 「函式呼叫函式」標示label[i][j]資訊
        ans = 0  # 計算答案「對應的面積」
        for i in range(N):
            for j in range(N):
                if label[i][j]==-1 and grid[i][j]==1:  # 還沒有走過
                    area = dfsArea(i, j)  # 第一輪，先算出面積
                    ans = max(ans, area)  # 單一最大面積，可能也是答案，記下來
                    dfsLabel(i, j, area, i*501+j) # 第二輪，再「標示」面積及「座標編號」
        for i in range(N):
            for j in range(N):
                if grid[i][j]==0:  # 遇到1個0，如果它變成1，能變成「好橋樑」連結2大塊嗎？
                    visited = set()
                    now = 1  # 自己本身若0變成1，可增加1格面積
                    for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                        if 0<=ii<N and 0<=jj<N and label[ii][jj]!=-1:
                            area, pos = label[ii][jj]  # 取出之前記錄的面積及「座標編號」
                            if pos not in visited:  # 連到「新大陸」
                                visited.add(pos)  # 記下新大陸的「座標編號」
                                now += area  # 加上「新大陸的面積」
                    ans = max(ans, now)
        return ans

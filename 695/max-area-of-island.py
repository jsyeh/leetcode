# 這題用簡單的 DFS 便能把「能走到的」都走到了！
# 先用 stack + while 迴圈來做
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # 了解長寬
        visited = [[False]*N for _ in range(M)] #走過不再走
        stack = [] # 用來 visiting()用的DFS資料結構
        def visiting(i, j):
            if i<0 or j<0 or i>=M or j>=N:
                return # 超過範圍，就略過
            if not visited[i][j] and grid[i][j]==1:
                stack.append((i,j)) # 能走的話
                visited[i][j] = True # 就過過去

        ans = 0
        for i in range(M): # 左手i
            for j in range(N): # 右手j
                if grid[i][j]==1 and not visited[i][j]:
                    visiting(i,j) # 能參訪，就參訪
                    now = 0
                    while len(stack)>0: # 繼續往4週參訪
                        i2,j2 = stack.pop()
                        now += 1
                        visiting(i2+1,j2)
                        visiting(i2-1,j2)
                        visiting(i2,j2+1)
                        visiting(i2,j2-1)
                    ans = max(ans, now)
        return ans

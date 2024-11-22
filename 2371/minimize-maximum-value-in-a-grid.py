# LeetCode 2371. Minimize Maximum Value in a Grid
# grid有不同的正數。在不改變「在同row或col」相對關係，可換新值
# 要讓 grid 裡「最大的值」最小。Hint 2 建議：從小到大，慢慢降值
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        # 可用 priority queue 來記錄「最小的數」在哪裡
        heap = []
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                heappush(heap, (grid[i][j], (i,j)))  # 記錄全部的值，將小到大取出

        rowMax, colMax = [0]*M, [0]*N  # 記錄row,col的最大值
        while heap:  # 只要 heap 裡還有值還沒處理
            oldVal, (i,j) = heappop(heap)  # 取出目前的最小
            now = max(rowMax[i], colMax[j]) + 1  # 要比現有的值，再+1
            grid[i][j] = now  # 更新值
            rowMax[i] = colMax[j] = now  # 再更新 row,col的最大值
        return grid

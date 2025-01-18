# LeetCode 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# 在 grid 裡，每格有4個方向：1向右、2向左、3向下、4向上。改變某1個方向，需要「花1點cost」。
# 想從0,0走到右下角。沒有路時，可「花1點cost」改變某1格的方向。請找到「最小cost」修改後，便能從0,0走到右下角。 
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # grid 的長寬
        table = [[inf]*N for _ in range(M)]  # 表格，用來存每一格的「最小cost」，預設值 inf 無限大
        table[0][0] = 0  # 表格中，出發點(0,0)的cost是0
        heap = [(0,0,0)]  # 利用 priority queue 進行 BFS，先放 cost是 0 的出發點(0,0)
        while heap:  # 只要 heap 還有座標在裡面，就繼續做
            cost, i, j = heappop(heap)
            if i==M-1 and j==N-1: return cost  # 更新到終點了，可以 return 答案
            for d, ii, jj in (1,i,j+1),(2,i,j-1),(3,i+1,j),(4,i-1,j):  # 往4個方向試
                if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 超過邊界，跳掉不處理
                w = 0 if grid[i][j]==d else 1  # 對應的 weighted cost，方向相同是 0，其他是 1
                if cost+w < table[ii][jj]:  # 現在推算出來的 cost 更小，便更新 table
                    table[ii][jj] = cost+w
                    heappush(heap, (table[ii][jj], ii, jj))  # 同時將座標放入 heap，以便更新
        return -1  # 沒找到答案（其實不用寫這行，因為一定在前面就會找到答案）

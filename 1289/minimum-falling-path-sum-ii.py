# 從最上面，每個 row 挑1個位置，往下掉時，逐個 row 要挑「與上一個row不同的col位置」
# 希望加起來最小。
# 這題應該可以簡單用 DP 做出來
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        # table = [[grid[i][j] for j in range(N)] for i in range(M)] # 複製grid值
        # table[i][j] 代表 在 row i 挑 col j 時，從上到下最小的值
        # 本來我還建了一個 DP table, 不過後來發現直接修改 grid[i][j]就好了
        for i in range(1,M): # table[0][j] 保留 grid[0][j] 的值，從i:1開始
            for j in range(N):
                currentMin = inf # 要找樓上最小值，先設無限大
                for k in range(N):
                    #if j!=k and table[i-1][k]<currentMin:
                    #    currentMin = table[i-1][k]
                    if j!=k and grid[i-1][k]<currentMin:
                        currentMin = grid[i-1][k]
                grid[i][j] += currentMin #table[i][j] += currentMin # 更新這個位置的值
        return min(grid[M-1][:]) #return min(table[M-1][:])

# LeetCode 3651. Minimum Cost Path with Teleportations
# m x n grid 從左上角移到右下角，2種移法：(1) 正常往右、往下，cost 是右邊、下面的值
# (2) 瞬間移動到 grid[x][y] <= 現在格子的值，最多行可瞬間移動 k 次。請找到「左上到右下」的最小 cost
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        cells = sorted( [grid[i][j], i, j] for i in range(M) for j in range(N))  # 依 grid[i][j] 來排序
        ptr = [0] * (k+1)  # 用了幾個 cells 裡的數
        heap = [(0,0,0,k)]  # 裡面放 (cost,i,j,k)，從0,0出發的 cost 是 0
        visited = {}  # 能快速找到「走到 (i,j,k)」的最小 cost
        while heap:  # 利用 heap 持續做，優先找 cost 小的
            cost, i, j, k = heappop(heap)
            if (i,j)==(M-1,N-1): return cost  # 能照優先順序，找到最小cost的走法
            if (i,j,k) in visited and visited[(i,j,k)] <= cost: continue
            visited[(i,j,k)] = cost
            if i<M-1 and ((i+1,j,k) not in visited or visited[(i+1,j,k)] > cost+grid[i+1][j]): 
                heappush(heap, (cost+grid[i+1][j], i+1, j, k) )  # （能走、沒走過/能更有效的走）往下走
            if j<N-1 and ((i,j+1,k) not in visited or visited[(i,j+1,k)] > cost+grid[i][j+1]): 
                heappush(heap, (cost+grid[i][j+1], i, j+1, k) )  # （能走、沒走過/能更有效的走）往右走
            if k>0:  # 若還有 k 可以用 teleport 瞬間移動
                val = grid[i][j]
                while ptr[k] < M*N and cells[ptr[k]][0] <= val:
                    cost2, i2, j2 = cells[ptr[k]]
                    if (i2,j2,k-1) not in visited or visited[(i2,j2,k-1)] > cost: 
                        heappush(heap, (cost, i2, j2, k-1) )  # （能走、沒走過/能更有效的走）
                    ptr[k] += 1
        return -1  # 這行可以不用寫

        # 下面的寫法，還是會超過時間
        M, N = len(grid), len(grid[0])
        heap = [(0,0,0,k)]  # 裡面放 (cost,i,j,k)，從0,0出發的 cost 是 0
        visited = {}  # 能快速找到「走到 (i,j,k)」的最小 cost
        while heap:  # 利用 heap 持續做，優先找 cost 小的
            cost, i, j, k = heappop(heap)
            if (i,j)==(M-1,N-1): return cost  # 能照優先順序，找到最小cost的走法
            if (i,j,k) in visited and visited[(i,j,k)] <= cost: continue
            visited[(i,j,k)] = cost
            if i<M-1 and ((i+1,j,k) not in visited or visited[(i+1,j,k)] > cost+grid[i+1][j]): 
                heappush(heap, (cost+grid[i+1][j], i+1, j, k) )  # （能走、沒走過/能更有效的走）往下走
            if j<N-1 and ((i,j+1,k) not in visited or visited[(i,j+1,k)] > cost+grid[i][j+1]): 
                heappush(heap, (cost+grid[i][j+1], i, j+1, k) )  # （能走、沒走過/能更有效的走）往右走
            if k>0:  # 若還有 k 可以用 teleport 瞬間移動
                for ii in range(M):  # 可以跳到哪裡？
                    for jj in range(N):  # 可以跳到哪裡？
                        if ii==i and jj==j: continue  # 避開原地跳、往回跳（左上區塊）
                        if grid[i][j]>=grid[ii][jj]:  # 合乎規定，能「瞬間移動」
                            if (ii,jj,k-1) not in visited or visited[(ii,jj,k-1)] > cost:
                                heappush(heap, (cost, ii, jj, k-1) )  # （能走、沒走過/能更有效的走）
        return -1  # 這行可以不用寫

        # 請教 AI 後，發現我的 DP 解法會超過時間、很難修正。建議我用 heap 解
        ''' 下面使用「函式呼叫函式」但 table太耗時，超過時間
        M, N = len(grid), len(grid[0])
        print(M,N)
        #return 0
        table = defaultdict(list)  # 對照表：有哪些瞬間移動的格子
        for i in range(M):
            for j in range(N):
                for ii in range(M):
                    for jj in range(N):
                        if (i,j)==(ii,jj): continue  # 避開原地跳
                        if grid[i][j]>=grid[ii][jj]:  # 能瞬間移動
                            table[(i,j)].append((ii,jj))
                print(len(table[(i,j)]))
        return 0
        @cache
        def helper(i,j,k):
            if i==M-1 and j==N-1: return 0
            ans = inf
            if i<M-1: ans = min(ans, grid[i+1][j] + helper(i+1,j,k))
            if j<N-1: ans = min(ans, grid[i][j+1] + helper(i,j+1,k))
            if k>0:
                for ii,jj in table[(i,j)]:
                    ans = min(ans, helper(ii,jj,k-1))
            return ans
        ans = helper(0,0,0)
        for kk in range(1,k+1):
            ans2 = helper(0,0,kk)
            if ans==ans2: return ans
            ans = ans2
        return ans # helper(0,0,k)
        '''
        ''' 下面不考慮 k 無法成功
        @cache
        def helper(i,j):
            if i==M-1 and j==N-1: return 0
            ans = inf
            if i<M-1: ans = min(ans, grid[i+1][j] + helper(i+1,j))
            if j<N-1: ans = min(ans, grid[i][j+1] + helper(i,j+1))
            return ans
        return helper(0,0)
        '''

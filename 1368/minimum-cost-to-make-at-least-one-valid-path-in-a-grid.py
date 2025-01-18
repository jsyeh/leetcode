# LeetCode 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# 在 grid 裡，每格有4個方向：1向右、2向左、3向下、4向上。改變某1個方向，需要「花1點cost」。
# 想從0,0走到右下角。沒有路時，可「花1點cost」改變某1格的方向。請找到「最小cost」修改後，便能從0,0走到右下角。 
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        graph = defaultdict(list)  # Hint 1 建議，建出 weighted graph 每格往4個方向
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                # 往 1,2,3,4 四個方向走
                for d,ii,jj in (1,i,j+1),(2,i,j-1),(3,i+1,j),(4,i-1,j):  # 方向、四個方向的座標
                    if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 超過邊界
                    if d==grid[i][j]:  # 方向相同
                        graph[(i,j)].append((0,ii,jj))  # weight是0
                    else:  # 方向不相同
                        graph[(i,j)].append((1,ii,jj))  # weight是1，需「1點cost」
        # 建好 graph 後，利用 cost (total weight) 來做 BFS
        heap = [(0, 0, 0)]  # cost 0, 站在出發點(0,0)
        visited = set()  # 走過的地方
        while heap:  # 只要還有「座標」在 heap 裡面
            cost, i, j = heappop(heap)  # 「取出」目前最小 cost 的位置
            if i==M-1 and j==N-1: return cost  # 用 heap 機制，以最小 cost 走到終點

            if (i,j) in visited: continue  # 若走過，就不要再走
            visited.add((i,j))  # 確認「現在」走過這個位置

            for w,ii,jj in graph[(i,j)]:  # 試試 weight graph 的4個方向（如果在邊、角，會更少）
                if (d, ii,jj) in visited: continue  # 若走過，避開
                heappush(heap, (cost+w, ii, jj))  # 加入 heap 待測試
        return -1  # 沒找到答案（其實不用寫這行，因為一定在前面就會找到答案）

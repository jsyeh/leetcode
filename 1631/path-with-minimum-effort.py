# 要找到一條PATH能有最小的diff值。但沒有想到「竟然能像蛇一樣繞」，所以改用heap來解
# （不能用DP來解）我有參考 hiepit 的 Solution
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        M, N = len(heights), len(heights[0])
        dist = [[math.inf]*N for _ in range(M)] 
        # dist[i][j] 此點 min path，都先存「無限大」
        dist[0][0] = 0 # 出發點 0, 0
        heap = [(0, 0, 0)] # (距離, i, j), 在出發點是 (0, 0, 0)
        # heapify(heap)

        while heap:
            d, i, j = heappop(heap) # 之前存在 heap 裡的最佳值
            if d > dist[i][j]: continue # 如果d值是舊的，放棄這組資料
            if i == M-1 and j == N-1: # 用最小的d值，走到右下角終點
                return d # 找到答案了
            
            directions = [[0,1],[0,-1],[1,0],[-1,0]] # 4個方向
            for di,dj in directions:
                i2, j2 = i+di, j+dj # 往4個方向的其中一個方向走
                if i2<0 or j2<0 or i2>=M or j2>=N: continue # 超過範圍

                d2 = max(d, abs(heights[i2][j2]-heights[i][j]))
                # 經由 i,j 到達 i2,j2 的新的 dist 值
                if d2 < dist[i2][j2]: # 如果能讓 dist[i2][j2] 更小的話
                    dist[i2][j2] = d2 # 更新
                    heappush(heap, (d2, i2, j2)) # 加入 heap

        return 0 # 這行應該不會執行到
'''
# 下面是錯誤的 DP 解法。但路線可能會繞，要換方法
        table = [[2000000]*N for _ in range(M)]
        table[0][0] = 0
        for i in range(M):
            for j in range(N):
                if i!=0:
                    table[i][j] = max(table[i-1][j], abs(heights[i][j]-heights[i-1][j]))
                if j!=0:
                    table[i][j] = min(table[i][j], max(table[i][j-1], abs(heights[i][j]-heights[i][j-1])))
        print(table)
        return table[M-1][N-1]
# case 8/75: [[3]] 只有1個點時
# case 9/75: [[1,10,6,7,9,10,4,9]]
# [[1,2,1,1,1]
# ,[1,2,1,2,1]
# ,[1,2,1,2,1]
# ,[1,2,1,2,1]
# ,[1,1,1,2,1]] 竟然有這樣繞的狀況!
'''

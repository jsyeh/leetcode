# LeetCode 1135. Connecting Cities With Minimum Cost
# 城市從1開始 1..n 在 connections 有 [x,y,cost] 對應「城市x城市y之間的cost]
# 可用 heap 
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        path = defaultdict(list)  # path[x] 對應「城市x」對外的資訊
        first = (inf, -1, -1)  # 最一開始的 edge 想找到「最小的edge」
        for x, y, cost in connections:  # 雙向連結
            path[x].append( (cost, y) )  # x 連到 y
            path[y].append( (cost, x) )  # y 連到 x
            first = min(first, (cost, x, y))  # 更新「最小的edge」
        cost, x, y = first  # 使用「最小的edge」
        visited = set( [x,y] )  # 標記「兩城市走過」
        ans = cost  # 累積的 cost
        heap = path[x] + path[y]  # 主要的 heap，內含 x 和 y 所有對外的路
        heapify(heap)  # 轉換成正確的 heap 資料結構
        while heap and len(visited)<n:  # 還有 heap 可進行，且「還沒做完」
            cost, x = heappop(heap)
            if x in visited: continue  # 走過的城市，避開，換下一個
            # 若是「未參訪的城市」，好好更新
            visited.add(x)  # 將「新城市x」加入「已參訪的城市」
            ans += cost  # 加入對應的 cost
            for cost, y in path[x]:  # 將「新城市x」所有對外的路
                heappush(heap, (cost, y))  # 全都加入 heap 裡
        if len(visited)==n: return ans
        else: return -1
        

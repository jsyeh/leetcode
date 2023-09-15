# 給定 [x,y] 座標, 找出"能把每個點連起來" 的長度, 距離是用 |x-x| + |y-y| 來算
# 使用 Minimum Spanning Tree，也就是每次先挑最短的，加上去
# 我有參考 idontknoooo 的 Solution 來思考
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x1, y1, x2, y2): # 用來算「曼哈頓距離」
            dx = abs(x1-x2)
            dy = abs(y1-y2)
            return dx+dy

        N = len(points)
        c = defaultdict(list) # 神奇資料結構，知道任何點的距離，將轉成 heap 結構
        for i in range(N):
            for j in range(i+1, N):
                d = dist(points[i][0], points[i][1], points[j][0], points[j][1])
                c[i].append((d,j)) # c[i] 會記「所有點到i的距離及編號
                c[j].append((d,i)) # c[j] 會記「所有點到j的距離及編號
        # 有了距離的資料結構
        visited = [False]*N # visited[i]表示 i是否已被visited
        ans = 0 # 目前累積的距離
        visitedN = 0 # 目前visited 的點的數目
        visited[0] = True # 先將點0標成「走過」當起點
        heap = c[0] # 先將點0 的連結狀況，加到 heap中，要找到裡面最小的距離的鄰居
        heapq.heapify(heap)
        # 開始探索答案，找出 Minimum Spanning Tree 的累積距離
        while heap: # 只要還有點在 heap裡，就繼續抓點出來
            d, i = heapq.heappop(heap)
            if not visited[i]: # 如果點i沒有被走過，便去走它
            # 意思是，如果i點已被走過，那個個 d, i 就不處理/丟掉的意思
                visited[i] = True
                visitedN += 1
                ans += d
                # 再來，便可將 i 牽連的鄰居，也都加到 heap 中
                for record in c[i]:
                    heapq.heappush(heap, record)
            if visitedN==N: break # 找齊全部的點，可以結束
        return ans


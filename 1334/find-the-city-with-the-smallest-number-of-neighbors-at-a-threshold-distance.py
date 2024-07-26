# LeetCode 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# 題目的英文很難懂：有n個城市，有edges裡有a,b,w 對應「城市a」與「城市b」的距離w
# 每個城市都能往外走，預算有限下，能走到幾個（別的）好鄰居的城市？鄰居很少的城市很孤單。
# 把「最孤單」的城市找出來。有多個城市「一樣孤單」時，回傳「編號」較的城市
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list) # 先建立 graph 資料結構
        for a,b,w in edges:  # 針對每1個 edge
            graph[a].append((b,w)) # 從a到b需要w的代價
            graph[b].append((a,w)) # 從b到a也需要w的代價
        ans = [] # ans[i] 對應「城市i」的好鄰居數量
        for i in range(n): # 針對每個城市，都要算他的「好鄰居」有幾個
            heap = [] # 可利用 Priority Queue (Heap) 來找最短路徑
            heappush(heap, (0, i)) # 先從 i 出發：到城市i，累積代價是0
            visited = set([i]) # 從 city i 出發，預算內「能經過哪些城市」（已走過i了）
            distance = [inf]*n # 到 從 i 到某 city 的距離，一開始是inf無限大
            while heap:  # heap 會先把（代價）小的找出來
                cost,a = heappop(heap) # 到達 城市a 需付出代價 cost
                if distance[a]<cost: continue # 答案沒有更短的話
                distance[a] = cost
                for b,w in graph[a]: # 城市a能到的城市
                    if cost+w<distance[b] and cost+w <= distanceThreshold: 
                        heappush(heap,(cost+w,b)) # 若「代價不超過範圍，且距離更短」就加入 heap
                        visited.add(b) # 並標記「能走到這個城市」（是好鄰居之一），避免重覆走
            ans.append((i,len(visited))) # 答案裡，記下 index 及「好鄰居」數量
        # ans.sort(key=lambda x:(x[1],-x[0])) # 答案排序的依據
        # return ans[0][0]
        lonely = min(ans, key=lambda x:(x[1],-x[0])) # 換個方法，希望更快
        return lonely[0]

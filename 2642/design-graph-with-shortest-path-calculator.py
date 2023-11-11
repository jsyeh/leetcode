class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        self.next = [[] for _ in range(n)] # next[v] 是 v 的下個點的list
        for src,target,cost in edges:
            self.next[src].append([target, cost]) # 同時存 taget 及對應的 cost

    def addEdge(self, edge: List[int]) -> None:
        src,target,cost = edge
        self.next[src].append([target, cost]) # 同上的作法

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2: return 0 # 同一個點，距離是0
        dist = [inf]*self.N # dist[v] 從node1到v的距離，一開始設「無限大」
        heap = [(0,node1)] # 因heap會看前面的數來排序，所以距離放前面
        # dist[node1] = 0 # 開始點，距離為0
        while len(heap)>0:
            cost, now = heappop(heap) # 現在最小的距離、對應的頂點
            if now==node2: return cost # 走到終點，得到答案
            if cost>dist[now]: # 距離沒有更短的話，這條走法沒有價值，
                continue

            dist[now] = cost # 可能更短的話，就更新，且繼續往下走
            for target2,cost2 in self.next[now]: # 從 now 出發到鄰居
                heappush(heap, (cost2+cost, target2)) # 新的距離
            # print(heap) # Debug 用，看 heap 變化狀況
        return -1 # 如果前面的while迴圈無法走到node2,就-1失敗


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

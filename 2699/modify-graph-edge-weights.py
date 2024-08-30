# LeetCode 2699. Modify Graph Edge Weights 題目：node 0..n-1, edges[i]有a,b,w 代表 a,b之間的weight
# 要把還沒設好的weight(-1)改成1以上的數，使得 src到dest的最短路徑值是target。把修改後的 edges 回傳。無法完成任務，就 return []
class Solution: # 如果沒有頭緒，可參考題目Description下方 Hint 1,2,3,4,5 
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        path = defaultdict(list)
        for a,b,w in edges: # 先建立「相連」關係
            path[a].append((w,b))
            path[b].append((w,a))
            if w==-1: # 如果是-1的話，就設成inf無限大吧！
                path[a][-1] = (inf,b)
                path[b][-1] = (inf,a)
        # Hint 1: 能從 source 走到 dest 嗎？（-1都當成inf無限大）
        def shortest_path():
            visited = [False] * n
            heap = [(0,source)]  # 從 source 出發
            while heap:
                dist, now = heappop(heap) # 目前最短距離
                if now == destination: return dist
                if visited[now]: continue
                visited[now] = True
                for w,b in path[now]:
                    heappush(heap,(dist+w, b))
            not_possible = True
            return inf
        not_possible = False
        path_length = shortest_path()
        if not_possible: return [] # 完全無法走到
        if path_length<target: return [] # 現有的路徑就已太短，也不行
        if path_length==target:  # 現有就很好，所以-1都填「最大值」
            return [[a,b,w] if w!=-1 else [a,b,2*10**9] for (a,b,w) in edges]
        # Hint 4: 如果有 edge 是a,b,-1 那 source到a的值dist1 + 由b到dest的值dist2 + w = target （沒寫完「最難的部分」）
        # 但是我想不出來怎麼寫。高手 awice 建議「頭到尾」用1、「尾到頭」用inf，邊做 dijkstra 邊記錄「每個node的parent及距離」
        # 把 edges 改成字典，將a,b改順序，最後順著遇到 -1 就改 edges[e] = max(target - distR.get(v, inf) - walked, 1)
        # 技巧太難了，我還是直接照著做吧
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        def dijkstra(source, adj, skip_negative):
            pq = [[0, source]]
            dist = defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heappush(pq, [d2, nei])

            return dist, parent
        
        distR, parentR = dijkstra(destination, adj, skip_negative=True)
        if distR.get(source, inf) < target:
            return []
        dist, parent = dijkstra(source, adj, skip_negative=False)
        if dist[destination] > target:
            return []
        
        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path = path[::-1]
        
        edges = {(min(u,v), max(u,v)) : w for u, v, w in edges}
        
        walked = 0
        for u, v in zip(path, path[1:]):
            e = (min(u, v), max(u, v))
            if edges[e] == -1:
                edges[e] = max(target - distR.get(v, inf) - walked, 1)
                if edges[e] > 1:
                    break
            walked += edges[e]
        
        for e, w in edges.items():
            if w == -1:
                edges[e] = 2 * (10 ** 9)
        
        return [[u,v,w] for (u,v), w in edges.items()]


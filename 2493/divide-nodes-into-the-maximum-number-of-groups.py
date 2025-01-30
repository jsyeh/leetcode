# LeetCode 2493. Divide Nodes Into the Maximum Number of Groups
# nodes 標示 1...n，若以 edges 相連的兩鄰居，需分在「相鄰」的 groups。問最多能分幾群 groups?
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:  # 先從 edges 變成 graph 結構
            graph[a].append(b)  # a 的鄰居有 b
            graph[b].append(a)  # b 的鄰居有 a
        # Hint 3 「最長」的距離，可用 BFS 算出來
        dist = [[-1]*(n+1) for _ in range(n+1)]  # dist[i][j] 從 i 到 j 距離
        for i in range(1,n+1):  # 用 BFS 把「每個node」對 node i 的距離算出來
            queue = deque() 
            queue.append([i,0])  # 從 node i 出發，對應「自己本身」的距離是 0
            dist[i][i] = 0
            while queue:
                a, d = queue.popleft()  # 現在 node a 與 node i 距離是 d
                for b in graph[a]:  # a 的鄰居 b
                    if dist[i][b] == -1:  # 沒有來過
                        dist[i][b] = d + 1  # 與 node i 的距離是 d + 1
                        queue.append([b,d+1])  # 再加入 queue 以便 BFS
        # Hint 1 建議檢查「graph 是否是 bipartite」。可再用 BFS 進行「著色挑戰」，看能否以2色著色/相鄰需不同色
        color = [-1]*(n+1)  # bipartite 著色，先放-1，之後著色成 color 0 或 color 1
        ans = 0  # 最後的答案（最多的 groups 數量）
        for i in range(1,n+1):  # 進行「著色挑戰」
            if color[i] != -1: continue  # 若此點已「著色」，就跳過
            member = set([i])  # 現在 connected component 的成員
            queue = deque([i])  # node 0 著色
            color[i] = 0  # node 0 著色成 color 0
            while queue:  # 利用 queue 進行 BFS，將 connected component 全部著色
                a = queue.popleft()  # node a 標示成 color c
                for b in graph[a]:  # node a 的鄰居 b
                    if color[b] == color[a]:  # 鄰居竟然同色，失敗
                        return -1  # 沒通過「著色挑戰」，就不是 bipartite graph 一定失敗
                    if color[b] == -1:  # 沒有來過，便需要著色
                        member.add(b)
                        queue.append(b)
                        color[b] = (color[a]+1) % 2  # 著另一種 color
            # 通過「著色挑戰」，此 group 是 bipartie。 Hint 2 把每個 connected component找「最長」的距離「加起來」
            maxDist = 0  # 這群 connected component 的最長距離（接下來查它們內的「最長」距離）
            for a in member:  # 現在 connected component 裡，暴力挑出 a
                for b in member:  # 暴力挑出 b
                    maxDist = max(maxDist, dist[a][b])  # 看 dist[a][b] 是不是最大的距離
            ans += maxDist + 1  # 最大距離，要再加上 node i 本身，共分成 maxDist + 1 個 groups
        return ans

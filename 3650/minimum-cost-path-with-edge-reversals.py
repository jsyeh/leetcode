# LeetCode 3650. Minimum Cost Path with Edge Reversals
# 從 edges[i] = [a,b,w] 對應 node a 到 node b 需 cost w
# 可反過來一次 node b 到 node a 需 cost w*2
# 問 node 0 到 node n-1 的最小 cost
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(defaultdict)
        for a,b,w in edges:  # 對應 node a 到 node b 需 cost w
            # 測資 698/699 有大量重覆的 edges 只留最小的
            if b not in path[a] or path[a][b]>w: path[a][b]=w
            if a not in path[b] or path[b][a]>w*2: path[b][a]=w*2
        heap = [(0,0)]  # 裡面對應 (cost,node)
        cost = [0] + [inf] * (n-1)  # 到達 node 的 cost
        while heap:  # 利用 heap 資料結構「持續做
            c, node = heappop(heap)
            if c > cost[node]: continue  # 若cost太高，換下一筆
            #cost[node] = c  # 更新 cost
            if node==n-1: return c  # 若到達終點，回傳對應 cost
            for node2 in path[node]:  # 繼續往下個點走
                if cost[node2] <= c + path[node][node2]: continue  # 避開
                cost[node2] = c + path[node][node2]  # 更新
                heappush(heap, (cost[node2], node2))
        return -1  # 沒走到終點，return -1 

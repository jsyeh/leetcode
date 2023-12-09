class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 先建立 path, list裡面藏 「下個點」及「色彩」
        path = defaultdict(list)
        for a,b in redEdges: # a可用紅線走到b
            path[a].append((b,0)) # 0:red
        for a,b in blueEdges: # a可用藍線走到b
            path[a].append((b,1)) # 1:blud

        # 使用 BFS 來找
        visited = [0]*2 # 兩種色彩
        visited[0] = [False]*n # 一開始都沒走過 Red 版
        visited[1] = [False]*n # 一開始都沒走過 Blue 版
        queue = deque()
        queue.append((0,0,0)) # 0點開始，0紅色，距離0
        queue.append((0,1,0)) # 0點開始，1藍色，距離0
        visited[0][0] = True # 出發點0走過了紅
        visited[1][0] = True # 出發點0走過了藍

        ans = [inf]*n # ans[i] 存0到i的距離
        ans[0] = 0 # 0到自己的距離是0

        while len(queue)>0: # BFS
            node, c, d = queue.popleft()
            for node2,c2 in path[node]:
                if c+c2==1: # 色彩不同
                    if not visited[c2][node2]:
                        visited[c2][node2] = True
                        queue.append((node2,c2,d+1)) # 下一步
                        ans[node2] = min(ans[node2],d+1) # 更短的距離

        for i in range(n): # 將 inf 變成 -1
            if ans[i]==inf: ans[i] = -1
        return ans


# LeetCode 2204. Distance to a Cycle in Undirected Graph
# n個node(0開始)，edges裡存node相連狀態，剛好有1個cycle。問「每個node到cycle的距離」
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        path = defaultdict(list)  # 先建出 path
        for a,b in edges:  # 針對 edge 的兩端點
            path[a].append(b)  # 各自加到對方的 path 裡
            path[b].append(a)
        # outside-in BFS, 持續把 inDegree 為 1 的「葉子」刪掉
        inDegree = [len(path[i]) for i in range(n)]  # 有幾個鄰取
        queue = deque()
        for i in range(n):
            if inDegree[i]==1:  # 「只有1個鄰居」叫「葉子」，待刪
                queue.append(i)
                inDegree[i] -= 1
        while queue:
            now = queue.popleft()  # 待刪的葉子
            for b in path[now]: # 葉子的鄰居，都裝
                if inDegree[b]>0: inDegree[b] -= 1  # 避開刪掉的葉子
                if inDegree[b]==1:
                    queue.append(b)
                    inDegree[b] -= 1
        # inside-out BFS，從cycle loop出發
        queue = deque()
        visited = set()
        for i in range(n):
            if inDegree[i]>0:  # 前面「還剩下的」就是 cycle loop
                queue.append((0,i)) # 把 circle 加入
                visited.add(i)
        ans = [0]*n
        while queue:
            dist, i = queue.popleft()
            ans[i] = dist  # 更新答案
            for b in path[i]:
                if b not in visited:  # 沒走過的話
                    queue.append((dist+1,b))  # 用 BFS 探索
                    visited.add(b)
        return ans

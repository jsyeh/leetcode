# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
# n 個城市，有n-1條路相接，原本 connections 裡「城市a」單向到「城市b」
# 但你需要將一些路「轉向」，讓「每條路都會到城市0」即「條條大路通羅馬」的意思
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        path = defaultdict(list)
        path2 = defaultdict(list)
        for a,b in connections:
            path[a].append(b)
            path2[b].append(a)
        queue = deque([0])
        visited = set([0])
        ans = 0
        while queue:
            now = queue.popleft()
            for j in path[now]:
                if j in visited: continue
                visited.add(j)
                queue.append(j)
                ans += 1
            for j in path2[now]:
                if j in visited: continue
                visited.add(j)
                queue.append(j)
        return ans

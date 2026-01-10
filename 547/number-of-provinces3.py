# LeetCode 547. Number of Provinces
# matrix isConnected 裡，有些是相連的。有幾個 connected component?
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        path = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if isConnected[i][j]:
                    path[i].append(j)
                    path[j].append(i)
        ans = 0
        visited = set()
        for i in range(N):
            if i in visited: continue
            visited.add(i)
            queue = deque([i])
            ans += 1
            while queue:
                now = queue.popleft()
                for j in path[now]:
                    if j not in visited: 
                        queue.append(j)
                        visited.add(j)
        return ans

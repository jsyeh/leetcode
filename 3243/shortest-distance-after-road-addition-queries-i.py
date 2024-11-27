# LeetCode 3243. Shortest Distance After Road Addition Queries I
# 0...n-1 共 n 個城市，i 可到 i+1，queries[i] = [a,b] 建捷徑
# 每次增加捷徑後，找到 0 到 n-1 的距離變多少。
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        for i in range(n-1):
            path[i].append(i+1)  # i 可到 i+1

        ans = []
        def helper():  # 幫忙找到答案
            visited = set()  # 接下來進行 BFS
            queue = deque()
            queue.append((0,0)) # 要0步，到達 city 0
            while queue:  # 利用 queue 進行 BFS 看「幾步後」到達目的地 city n-1
                step, city = queue.popleft()
                for city2 in path[city]:
                    if city2==n-1:  # 到達目的地
                        ans.append(step+1)  # 找到答案，並結束
                        return
                    if city2 not in visited:  # 只要還沒走過
                        visited.add(city2)  # 就排入 BFS 之後再探索
                        queue.append((step+1,city2))
        for a,b in queries:
            path[a].append(b)  # 加入1條新的 path
            helper()  # 再次探索、找答案
        return ans

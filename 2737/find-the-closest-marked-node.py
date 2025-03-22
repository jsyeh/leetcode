# LeetCode 2737. Find the Closest Marked Node
# 從 s 開始，找到最近的 marked node
class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        marked = set(marked)  # 變成 set() 找得更快
        path = defaultdict(list)
        for a,b,w in edges:  # 小心，是單向的 edge 哦！
            path[a].append((b,w))
        visited = set()
        heap = [(0,s)]  # node s 出發，距離0
        while heap:
            dist, node = heappop(heap)
            if node in marked:
                return dist
            if node in visited: continue
            visited.add(node)
            for b,w in path[node]:
                heappush(heap, (dist+w, b))
        return -1

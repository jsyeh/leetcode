# LeetCode 261. Graph Valid Tree
# 0..n-1個 nodes 能否用 edges 接成 tree 即「最精簡的edges」
# 也就是從 0 出發，可用 n-1 個 edges 走達「每一個node」
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:  # 如果數量不符合
            return False  # 就失敗

        graph = defaultdict(list)  # 從 edges 建出 graph
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        stack = [0]  # 利用 stack 進行 DFS
        visited = set([0])  # 從 0 出發，能走到哪些 nodes
        while stack:
            a = stack.pop()  # DFS 挑出1個繼續走
            for b in graph[a]:  # 能走到的 nodes
                if b in visited: continue  # 走過，不走
                stack.append(b)  # 再排入 stack 進行 DFS
                visited.add(b)  # 多走到1個node
        return len(visited)==n  # 最後是否到達「全部的點」     

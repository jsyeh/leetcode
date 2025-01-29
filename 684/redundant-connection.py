# LeetCode 684. Redundant Connection
# n nodes, 標成 1..n，基本上只要 n-1 個 edges 就能連起來。
# 但給 n 個 edges 所以會有 1 個 edge 是可拔除的。把它找出來。
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)  # 逐一加入 edge 慢慢建出 graph 資料結構
        for ei,(a,b) in enumerate(edges):  # edge id, a, b
            graph[a].append((b,ei))
            graph[b].append((a,ei))
            # 每次加一個 edge，加完後，用 DFS 測試「是否有loop發生」
            visited = set([a])  # 從 a 出發
            usedEdge = set()  # 想知道過程中，用了哪些 edge（都只用一次）
            def dfs(a):  # 「函式呼叫函式」的 DFS 函式，從 node a 出發，會不會「走到重覆的點」
                for b,ei in graph[a]:
                    if ei in usedEdge: continue  # 走過的 edge 不要再走
                    if b in visited and ei not in usedEdge:  # 不同路，卻能走到同一node
                        return True  # 就是有重覆，失敗
                    visited.add(b)
                    usedEdge.add(ei)
                    if dfs(b): return True
                return False
            if dfs(a):  # 如果 dfs()後，發現有cycle loop發生，表代「這個edge是多餘的」
                return edges[ei]  # return 這個「多餘的edge」

# LeetCode 323. Number of Connected Components in an Undirected Graph
# 有幾個 connected components? 使用 BFS 或 DFS 即可
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        for a,b in edges:  # 先建出 path 資料結構
            path[a].append(b)
            path[b].append(a)
        visited = set()  # 走過的，就不用再走
        ans = 0  # 有幾區
        def dfs(i):  # 函式呼叫函式
            for b in path[i]:  # 順著 i 往外走
                if b not in visited:  # 鄰居 b 若沒走過
                    visited.add(b)  # 標示走過
                    dfs(b)  # 函式呼叫函式，再往外走
        for i in range(n):  # 針對所有的 node
            if i not in visited:  # 若沒走過
                ans += 1  # 找到1個新答案
                visited.add(i)  # 標示走過
                dfs(i)  # 函式呼叫函式，再往外走
        return ans

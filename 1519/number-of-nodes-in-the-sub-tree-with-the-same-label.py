# LeetCode 1519. Number of Nodes in the Sub-Tree With the Same Label
# n nodes (0..n-1) 其中 node 0 是 root。用 edges 接成 tree 結構。
# 想找出每個 node i 對應的「sub-tree」裡，有幾個 nodes 的 label 與 node i 相同
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        freq = [Counter() for i in range(n)]  # 每個小孩對應字母頻率
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()  # 走過的，不要再走
        ans = [0] * n  # 最後放答案
        def dfs(root):  # 函式呼叫函式，更新 ans[root]
            visited.add(root)  # 走過的，不要再走
            label = labels[root]  # 對應的 label
            for child in graph[root]:
                if child in visited: continue  # 走過，不壩走
                dfs(child)  # 更新這個分支
                freq[root] += freq[child]  # 將 freq 合併
            freq[root][label] += 1  # 更新自己
            ans[root] = freq[root][label]  # 填入答案
        dfs(0)  # 函式呼叫函式，從 root 開始，全部做一次
        return ans         

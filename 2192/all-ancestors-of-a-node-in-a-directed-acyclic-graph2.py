# LeetCode 2192. All Ancestors of a Node in a Directed Acyclic Graph
# 改用「函式呼叫函式」來進行DFS深度優先搜尋
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        A = defaultdict(list)  # A[b] 裡面會有 b 的可能祖先
        for a, b in edges:  # edges 裡有一堆 a 往 b 的連線
            A[b].append(a)  # a 可以走到b
        
        ans = [ [] for i in range(n) ] # 用來放答案的「一堆list」
        def dfs(i, visited):  # 利用「函式呼叫函式」進行 DFS
            if i in visited: return []
            visited.add(i)
            ans = [i]
            for parent in A[i]:
                if parent not in visited:
                    ans += dfs(parent, visited)
            return ans
        for i in range(n):  # 逐一探討 node i 的祖先可能有誰
            visited = set() # 一開始還沒有visited過
            for parent in A[i]: ans[i] += dfs(parent, visited) # 要累積 node i 的全部祖先
            ans[i].sort()  # 利用「函式呼叫函式」進行 DFS
        return ans

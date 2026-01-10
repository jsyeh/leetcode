# LeetCode 399. Evaluate Division
# 給你很多「除法a/b」的值，再問你queries「除法」的結果
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            path[a].append((b,values[i]))
            path[b].append((a,1/values[i]))
        def helper(a, b):
            visited.add(a)
            for c, v in path[a]:
                if c==b: return v
                if c in visited: continue
                now = helper(c,b)
                if now != -1: return v * now
            return -1
            
        ans = []
        for a, b in queries:
            if a not in path or b not in path: ans.append(-1)  # 找不到
            else:  # 要利用 DFS 找答案
                visited = set()
                ans.append(helper(a,b))
        return ans

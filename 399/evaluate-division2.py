# LeetCode 399. Evaluate Division
# 給你很多「除法a/b」的值，再問你queries「除法」的結果
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        table = defaultdict(list)
        for (a,b),v in zip(equations, values):
            table[a].append((b, v))
            table[b].append((a, 1/v))
        ans = []
        for a,b in queries:
            if a==b and table[a]:
                ans.append(1.0)
                continue
            queue = deque()
            queue.append((a,1))
            visited = set([a])
            theAns = -1
            while queue:
                now, v = queue.popleft()
                for c, v2 in table[now]:
                    if c in visited: continue
                    if c==b: 
                        theAns = v*v2
                        queue.clear()
                        break
                    visited.add(c)
                    queue.append((c, v*v2))
            ans.append(theAns)
        return ans

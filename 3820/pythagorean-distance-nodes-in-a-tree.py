# LeetCode 3820. Pythagorean Distance Nodes in a Tree
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        path = defaultdict(list)
        for a,b in edges:
            path[a].append(b)
            path[b].append(a)
        def findDist(x):
            dx = {x:0}
            queue = deque([(0,x)])
            while queue:
                step, a = queue.popleft()
                for b in path[a]:
                    if b in dx: continue
                    dx[b] = step+1
                    queue.append((step+1,b))
            return dx
        dx = findDist(x)
        dy = findDist(y)
        dz = findDist(z)
        ans = 0
        for i in range(n):
            a,b,c = sorted([dx[i],dy[i],dz[i]])
            if a*a+b*b==c*c:
                ans += 1
        return ans

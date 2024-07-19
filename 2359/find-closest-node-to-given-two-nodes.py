# LeetCode 2359. Find Closest Node to Given Two Nodes
# 有一堆 node，每個node（最多）只有1個往外的edge。
# 想知道 node1...node2 中間的點是誰。但要小心有cycle發生
# 可從 node1 和 node2 同時 BFS 出發，看在什麼時候相撞，就是答案
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        queue = deque()  # 用來進行 BFS 將 node1 和 node2 展開
        queue.append((node1,0,0))  # node1 走到 node1 要花 0 步
        queue.append((node2,1,0))  # node1 走到 node1 要花 0 步
        visited = [set(), set()]  # 分別走過的地方
        visited[0].add(node1)
        visited[1].add(node2)
        table = [defaultdict(int), defaultdict(int)] # 用來查「某個點」對應的step數

        while queue:
            now,start,step = queue.popleft()  # 依序吐出 BFS queue
            table[start][now]=step # 標示對應的step數
            next = edges[now] # 下一個要去的地方
            if next != -1 and next not in visited[start]: # 沒走過
                visited[start].add(next)
                queue.append((next,start,step+1))
        ans = -1
        ansStep = inf  # 無限大
        for i in range(len(edges)): # 針對每一個 node 查它們的 step值
            if i in table[0] and i in table[1]:
                if max(table[0][i], table[1][i]) < ansStep:
                    ansStep = max(table[0][i], table[1][i])
                    ans = i
        return ans
# case 11/77: edges = [5,4,5,4,3,6,-1], node1 = 0, node2 = 1
# case 76/77: edges = [1,0] node1 = 0, node2 = 1

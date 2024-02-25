# diameter: tree 裡「最長的path」有多少 eddge
# 10^4 nodes, Input 只有一堆 edges 所以不知道「誰在上、誰在下」
# 因為「數字不重覆」所以可建 dict
# 先「任一點」BFS 找到最遠的點（端點1），再從端點1 BFS 走到最遠的端點2
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        N = len(edges)+1 # Node數量，比edges數量+1
        # 建 edges fromTo 資料
        fromTo = defaultdict(list)
        for a,b in edges:
            fromTo[a].append(b)
            fromTo[b].append(a)
        # 接下來從 0 開始走
        visited = [False]*N
        queue = deque()
        queue.append(0)
        visited[0] = True
        while len(queue)>0:
            now = queue.popleft()
            ans1 = now # 想找出最遠的端點1
            for node in fromTo[now]: # 往鄰居探索
                if visited[node]==False: # 如果沒探索過
                    queue.append(node) # 就加入queue
                    visited[node] = True # 並標示「走過了」避免重覆走
        
        visited = [False]*N
        queue.append((ans1,0)) # 將端點1加入，要找到端點2的距離
        visited[ans1] = True
        while len(queue)>0:
            now, dist = queue.popleft() # 這次多吐出「距離」
            ans = dist # 隨時更新「最遠的距離」
            for node in fromTo[now]: # 往鄰居探索
                if visited[node]==False: # 如果沒探索過
                    queue.append((node,dist+1)) # 就加入queue
                    visited[node] = True # 並標示「走過了」避免重覆走
        return ans

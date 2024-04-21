# 想知道 vertex 0 能不能走到 最後的 vertex n-1
# 總共有2*10^5個頂點。可以利用 Hash Set，看 0 能到哪些地方
# 另外也可以先建出 鄰居的 hash set 以便 BFS 或 DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1: return True # 如果只有一個頂點，起點0 剛好是終點 n-1 成功
        neighbor = collections.defaultdict(list) # 鄰居的資料結構
        for a,b in edges: # 建出「鄰居」的資料結構
            neighbor[a].append(b)
            neighbor[b].append(a)
        visited = set() # 能到達的點
        queue = collections.deque()
        queue.append(source) # 加入 queue 的同時，也加入 visited
        visited.add(source)
        while len(queue)>0:
            a = queue.popleft() # BFS 接下來要出發的點
            for b in neighbor[a]:
                if b == destination: return True # 剛好是終點 n-1
                if b not in visited: # 沒有走過的話，便要去走訪
                    queue.append(b) # 加入 queue 的同時，也加入 visited
                    visited.add(b)
        return False # 走完，卻都沒成功，便是失敗
# case 27/30: n=10, edges=[[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]]
# source=1, destination=0 原來可任意挑定 source 及 destination

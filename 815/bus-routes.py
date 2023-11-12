# 這個題目看似很難，不過我在2023-05-05 寫過，即參考過lee215的解法
# 作法的精華，是先做出對照表，知道「每一個公車站牌」有哪些路線經過
# 再利用 BFS 的方法，從「出發點」開始，將「公車站牌」塞進queue
# popleft() BFS 取出站牌，再把「它經過的路線」裡的每個站版，再加回queue
# 但為避免「重覆走」，需要 visited 及 visited_route 不再走「走過的路」及「走過的站牌」
# 為了知道答案（要轉乘幾次），所以 queue 裡還要再記「轉乘次數」
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0 # 有個陷阱「開始結束同一點」

        d = defaultdict(list) # d[stop] 會得到站牌對應的路線
        for i in range(len(routes)): # 先建資料結構
            route = routes[i] 
            for stop in route: # 把每條路線的每個站牌 
                d[stop].append(i) # 都加到 d[stop] 裡
        # print(d) # debug用

        visited = set() # visited stop 走過的站牌，不重覆走
        visited_route = set() # 走過的路線，不重覆走
        queue = deque() # 用來 BFS 的 queue 資料結構
        queue.append((1, source)) # 先把起點加入 queue
        visited.add(source) # 走過的點，以後不會再走
        while len(queue)>0: # BFS 一直做
            dist, now = queue.popleft() # queue會存距離、點
            for i in d[now]: # 現在的站牌，對應的多條路線
                if i in visited_route: continue # 不走重覆路線
                visited_route.add(i) # 現在這條，標示走過
                for next in routes[i]: # 路線中全部的點
                    if next == target: return dist # 走到，回傳距離
                    if next not in visited: # 路線中沒走過的點
                        queue.append((dist+1, next)) # 加入queue
                        visited.add(next) # 同時標示走過不再走
        return -1 # BFS 沒提早結束，表示走不到
        

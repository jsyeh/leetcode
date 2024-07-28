# LeetCode 2093. Minimum Cost to Reach City With Discounts
# highways 裡，有一 city1, city2, toll 過路費資訊。discount 挑路線（費用減半），每條路能用1次。
# 問 city 0 到 city n-1 最少要多少錢？用 priority queue應可解。但 discount 很麻煩。
# 參考 znathan 的解法，很巧妙的把 discount ticket 也加入 heap 的參數。
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)  # 先建出 graph
        for c1,c2,toll in highways:  # 從 c1 到 c2 需過路費 toll
            graph[c1].append((toll,c2))
            graph[c2].append((toll,c1))
        heap = []
        heappush(heap, (0,0,discounts) ) # 從 city 0 到 city 0 需要 0 元，沒用掉任何 折價卷
        visited = {}
        while heap:
            total, now, tickets = heappop(heap) # 目前到 now 需要 total 元, 剩下 折價卷
            if now in visited and visited[now]>=tickets:
                continue # 這個城市，在更便宜的時候，就用更少的tickets走過，那就不用再探訪了
            visited[now] = tickets # 現在的等級
            if now==n-1: return total # 以最少的經費，到達目的地
            for toll,c2 in graph[now]:
                heappush(heap, (total+toll,c2,tickets))  # 不使用 discount ticket 折價卷
                if tickets>0: heappush(heap, (total+toll//2, c2, tickets-1)) # 使用 折價卷
        return -1

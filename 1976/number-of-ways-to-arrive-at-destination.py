# LeetCode 1976. Number of Ways to Arrive at Destination
# 0..n-1 共 n 個城市，roads[i] 將a,b城市連起來,距離是t（要花t分鐘才能到達）
# 從 0 到 n-1「最短路徑」有幾條（答案太大，要取(10^9+7)的餘數）
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9+7
        shortest = [inf] * n  # 最短路徑（一開始「無限大」以便更新）
        ways = [0] * n  # 能走到 city i 最短路徑走法，一開始是0個

        path = defaultdict(list)
        for a,b,t in roads:  # a,b兩城市，有條路需t分鐘
            path[a].append((t,b))
            path[b].append((t,a))
        heap = [(0,0)]  # 距離0，在出發點0
        ways[0] = 1  # 出發點，有1種走法
        while heap:
            dist, city = heappop(heap)
            if dist > shortest[city]: continue  # 沒有更短，不用看它
            for t,b in path[city]:  # 從 city 到「城市b」需t分鐘
                if dist + t < shortest[b]:  # 若能更快到達 city b
                    shortest[b] = dist + t  # 更新
                    ways[b] = ways[city]  # 到 city 有幾種走法，就能再走到b
                    heappush(heap, (dist+t,b))  # 新的走法，加到 heap 裡
                elif dist + t == shortest[b]:  # 若距離相同，也是最短路徑
                    ways[b] = (ways[b] + ways[city]) % MOD  # 就更新 ways[b]
        return ways[n-1]  # 從 0 出發，到 city (n-1) 「最短路徑」有幾種走法.....

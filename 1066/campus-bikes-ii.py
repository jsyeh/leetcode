# LeetCode 1066. Campus Bikes II
# 找到 workers 和 bikes 關係，每個 worker 要騎1台車。
# workers[i] 走到 bikes[j] 的距離（只能直走、橫走，不能斜走）加起來最短
# 雖只 10 台車，但不能暴力法，因 10! 太大！可用 Heap 來優先處理「比較小的cost」展開
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(i, j):
            return abs(workers[i][0]-bikes[j][0]) + abs(workers[i][1]-bikes[j][1])
        heap = [[0, 0, 0]]  # cost是0，處理第i個worker，沒有騎走任一台車bitmask
        visited = set()  # 有哪些已處理過的重覆狀況，就不用再處理
        while heap:
            cost, i, bitmask = heappop(heap)  # bitmask 對應「哪幾台車被騎走了」
            if (i, bitmask) in visited: continue  # 處理過了，不需要再處理
            visited.add((i, bitmask))

            if i==len(workers): return cost  # 處理完全部人，優先得到「比較小」的cost！成功！
            for j in range(len(bikes)):  # bikes[j]
                if bitmask & (1<<j) == 0:  # 還沒被騎走，可試試
                    heappush(heap, [cost+dist(i,j), i+1, bitmask | (1<<j)])  # 可試騎

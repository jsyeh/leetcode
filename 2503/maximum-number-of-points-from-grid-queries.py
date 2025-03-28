# LeetCode 2503. Maximum Number of Points From Grid Queries
# 很大的二維陣列 grid 裡，問 queries[i] 從左上角出發，能蓋掉哪些數字？
# 理論上 BFS 就能解，沒想到第 17/21 測資會超時，因為 queries 量太大了
# Hint 建議 queries 先 sort，再小到大依序求解，最後照原來的順序放回即可
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])  # 先知道長寬，方便之後 Best First Search
        table = {}  # 照 Hint 建議打亂 queries 順序，用 table 存放答案，之後照順序排好
        q2 = sorted(queries)  # 讓「新的 queries」從小到大排好，再「從小到大解題」

        heap = []  # 利用 Heap/Priority Queue 進行 Best First Search
        heappush(heap, (grid[0][0], 0,0) )  # 先把「左上角」放入 heap 當「起點」，附上值
        visited = set()  # 在 BFS 或 Best First Search 時，不會重覆將「格子」放入 heap 裡
        visited.add( (0,0) )  # 標示「左上角」已放入 heap 
        now = 0  # 現在「能合格走過」的數量，迴圈前面是 0
        for q in q2:  # 照著「新的 queries」從小到大「依序加大」能走到的範圍
            while heap and heap[0][0]<q:  # 若 heap 還有「目前能走到」、能用「新的 queries」蓋掉/走過
                now += 1  # 那就多一個「能合格走過」的格子
                v, i, j = heappop(heap)  # 將這個格子「移出 heap」，再往「四個方向」加大 heap 
                for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 下、上、右、左 四個方向
                    if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 若超過格子範圍，就跳過
                    if (ii,jj) in visited: continue  # 若走過，就跳過
                    heappush(heap, (grid[ii][jj], ii,jj) )  # 將「能走」的鄰居，放入 heap 
                    visited.add( (ii,jj) )  # 並標示這個鄰居，避免之後重覆加入 heap
            table[q] = now  # 這輪算出來的「累積答案」，放入 table 對照表
        # 全部「新的 queries」都算完後，利用下面的倒裝句，照「原來的順序」放入 answer 裡
        answer = [table[q] for q in queries]
        return answer  # 照「原來的順序」的 answer 當答案 （上下2行可合成一行，我只是故意分2行）

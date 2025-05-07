# LeetCode 3341. Find Minimum Time to Reach Last Room I
# n x m 地下城裡, 有些房間(格子)一開始不能進入, 要等到 moveTime[i][j] 對應時間後,才能進入
# 請問最快最快,是要多久才能進入「最後的房間 (n-1, m-1)」
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])  # 先知道地圖的長、寬
        heap = []  # 可利用 priority queue 來解這題
        heappush(heap, (0, 0, 0))  # 一開始在第0秒, 待在 0,0 的房間
        visited = set()  # 走過的房間, 就不用再走
        visited.add((0,0))  # 有走過 (0,0)這個房間
        while heap:  # 持續進行模擬
            t, i, j = heappop(heap)  # 現在最快的時間在這裡
            if i==N-1 and j==M-1: return t  # 最快的速度, 找到最後1格(終點)

            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 往4個方向走
                if ii<0 or jj<0 or ii>=N or jj>=M: continue  # 超過邊界的, 不走
                if (ii,jj) in visited: continue # 走過的, 不走
                # 將可在某個時間(的下一個時間點), 走到ii,jj這格
                heappush(heap, (max(t,moveTime[ii][jj])+1, ii, jj) ) 
                visited.add((ii,jj))  # 這格進入 heap 就不能再走進來哦

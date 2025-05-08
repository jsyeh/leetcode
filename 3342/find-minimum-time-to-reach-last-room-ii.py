# LeetCode 3342. Find Minimum Time to Reach Last Room II
# 從 (0,0) 出發，地下城的房間 (i,j) 在 moveTime[i][j] 才會開放
# 但「移動的時間」卻是 1秒、2秒、1秒、2秒，這樣間隔，問最快何時到 (n-1,m-1) 
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])
        heap = []
        heappush(heap, (0, 0, 0, 1))  # 多參數1，對應「要花1秒走」
        visited = set()
        visited.add((0,0))  # 起點，走過
        while heap:
            t, i, j, s = heappop(heap)
            if i==N-1 and j==M-1: return t
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=N or jj>=M: continue
                if (ii,jj) in visited: continue
                tt = max(t, moveTime[ii][jj])
                heappush(heap, (tt+s, ii, jj, 3-s))
                visited.add((ii,jj))

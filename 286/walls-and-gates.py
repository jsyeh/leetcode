# LeetCode 286. Walls and Gates
# m x n 的陣列 rooms[i] 有3種值：-1:牆 0:gate門 2147483647:空房間
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        M, N = len(rooms), len(rooms[0])  # 長、寬
        queue = deque()
        for i in range(M):
            for j in range(N):
                if rooms[i][j]==0: 
                    queue.append((0,i,j))
        while queue:
            d, i, j = queue.popleft()
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: continue
                if rooms[ii][jj]==2147483647:
                    rooms[ii][jj] = d + 1
                    queue.append((d+1,ii,jj))

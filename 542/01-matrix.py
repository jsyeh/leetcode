class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        dist = [[0]*N for _ in range(M)]
        Q = deque() # 使用 deque 的 append() 與 popleft() 來實作 Queue
        for i in range(M):
            for j in range(N):
                if mat[i][j]==0: Q.append((i,j,0))
        
        def testAndPush(i:int, j:int, step:int):
            if i<0 or j<0 or i>=M or j>=N: return
            if mat[i][j]==1 and dist[i][j]==0: # 能走，且還沒走到
                dist[i][j] = step
                Q.append((i,j,step))

        while len(Q)>0:
            i,j,step = Q.popleft()
            testAndPush(i+1,j,step+1)
            testAndPush(i-1,j,step+1)
            testAndPush(i,j+1,step+1)
            testAndPush(i,j-1,step+1)

        return dist

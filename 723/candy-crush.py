# 模擬題，要模擬連3個要消掉。接著往下掉，再模擬連3個要消掉，直到結束。
# 最多就50x50，所以模擬不會超時
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        M = len(board)
        N = len(board[0])
        print(M,N)

        dI = [0,1,0,-1]
        dJ = [1,0,-1,0]
        def findSame(val, i, j, d, repeat)->int: # return the length
            if i<0 or j<0 or i>=M or j>=N: return repeat
            if val == 0: return repeat # 如果已經空了，就不要找了
            if board[i][j]==val:
                return findSame(val, i+dI[d], j+dJ[d], d, repeat+1)
            else: return repeat

        def crush(i, j, d, Len): # 照著之前在 queue 裡記錄的點，照著方向長度消消消
            for k in range(Len):
                board[i][j] = 0
                i += dI[d]
                j += dJ[d]

        queue = deque()
        def findSameAndCrush()->bool: # 
            for i in range(M):
                for j in range(N):
                    for d in range(2): # 只試2個方向（因迴圈走法，剛好可行
                        Len = findSame(board[i][j], i, j, d, 0)
                        if Len >= 3:
                            queue.append([i,j,d,Len])# 加入 Queue裡，以便之後刪除
            if len(queue)==0: return False
            while len(queue)>0:
                i, j, d, Len = queue.pop()
                # print(i,j,d,Len)
                crush(i,j,d,Len)
            return True

        def drop():
            for i in range(1,M): # 由1往下巡，最上面一層的洞，不用補就跳過
                for j in range(N):
                    if board[i][j]==0:
                        for k in range(i, 0, -1):
                            print("i,j,k:", i, j, k)
                            board[k][j] = board[k-1][j]
                        board[0][j] = 0 # 掉下後，最上面就空了

        while findSameAndCrush(): # 如果有 find and crush
            drop() # 就往下掉

        return board

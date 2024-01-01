# 模擬的遊戲，更新完 board 即可
# 太孤單，會死。太擠，會死。只有剛好2-3個鄰居，不會死。
# 如果有3個鄰居，那死會復生。
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        M, N = len(board), len(board[0])
        board2 = [[0]*N for _ in range(M)]

        def neighborN(i, j): # 查 board[i][j] 的鄰居有幾個
            ans = 0
            for ii in range(max(0,i-1), min(M, i+2)):
                for jj in range(max(0,j-1), min(N, j+2)):
                    if board[ii][jj]==1: ans += 1
            return ans - board[i][j]

        # 接下來從 board 更新 board2
        for i in range(M):
            for j in range(N):
                neighbor = neighborN(i, j)
                if board[i][j]==0 and neighbor==3:
                    board2[i][j] = 1 # 復活
                elif board[i][j]==1 and (neighbor==2 or neighbor==3):
                    board2[i][j] = 1 # 繼續活
                else:
                    board2[i][j] = 0 # 死掉

        # 只要模擬1次，再把答案copy 填回 board
        for i in range(M):
            for j in range(N):
                board[i][j] = board2[i][j]
        """
        Do not return anything, modify board in-place instead.
        """

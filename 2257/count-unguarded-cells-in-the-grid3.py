# LeetCode 2257. Count Unguarded Cells in the Grid
# 在 m x n 的格子裡，有幾個格子，是 Guard 看不到的？
# G 是 Guard, W 是 Wall, 問 m x n 有幾個格子「不會被 Guard 看到」
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0]*n for _ in range(m)]  # 0 表示還沒走過，1卡住，2被看到
        for i,j in guards:  # guard 的位置
            board[i][j] = 1  # 會卡住
        for i,j in walls:  # wall 的位置
            board[i][j] = 1  # 也會卡住
        # 建好會擋住的 guard 和 wall 後，開始巡視
        for i,j in guards:  # 每個 guard 往4個方向看
            for k in range(i+1, m):
                if board[k][j]==1: break
                board[k][j] = 2
            for k in range(i-1, -1, -1):
                if board[k][j]==1: break
                board[k][j] = 2
            for k in range(j+1, n):
                if board[i][k]==1: break
                board[i][k] = 2
            for k in range(j-1, -1, -1):
                if board[i][k]==1: break
                board[i][k] = 2
        # 最後再數一下，有幾格「還是0」（沒被巡視到）
        return sum(row.count(0) for row in board) 

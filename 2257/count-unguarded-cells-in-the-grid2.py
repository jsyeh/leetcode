# LeetCode 2257. Count Unguarded Cells in the Grid
# 在 m x n 的格子裡，有幾個格子，是 Guard 看不到的？
# G 是 Guard, W 是 Wall, 問 m x n 有幾個格子「不會被 Guard 看到」
# 有 10^5 格子，所以不能暴力去巡Guard可以看到的格子。
# 又 guard 和 wall 最多有 5*10^4 也是超大，真麻煩
# 但看 Solutions 發現「標示wall及guard」位置，並中斷迴圈，最多只要走10^5格
# 所以開始寫
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0]*n for _ in range(m)] # 0 表示還沒走過，1卡住，2被看到
        for i,j in guards: # guard 的位置
            board[i][j] = 1 # 會卡住
        for i,j in walls: # wall 的位置
            board[i][j] = 1 # 也會卡住
        # 建好會擋住的 guard 和 wall 後，開始巡視
        dI = [0,1,0,-1] # 移動的方向
        dJ = [1,0,-1,0]
        for i,j in guards:  # 針對每一個 Guard 往四週發展
            for d in range(4): # 往4個方向巡視
                ii, jj = i+dI[d], j+dJ[d]
                while ii>=0 and jj>=0 and ii<m and jj<n and board[ii][jj]!=1: # 沒有被wall或guard擋住的話
                    board[ii][jj] = 2 # 會被參訪巡視
                    ii, jj = ii+dI[d], jj+dJ[d]
        # 最後再數一下，有幾格「還是0」（沒被巡視到）
        return sum(row.count(0) for row in board)
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]==0: ans += 1 # 有幾個還是0（沒被巡視到）
        return ans

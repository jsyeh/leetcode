# LeetCode 2664. The Knight’s Tour
# m x n 的棋盤上，騎士在 (r,c) 座標，要把「棋盤每一格」走過
# 因 m, n <= 5 總共25格，可用 backtrack 回溯法完成
class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1]*n for _ in range(m)]  # 待走的棋盤
        self.steps = 0  # 目前走了0步
        def helper(r,c):
            if r<0 or c<0 or r>=m or c>=n:
                return False  # 超過邊界，失敗
            
            if board[r][c]==-1:  # 如果這格還沒走過，就試走
                board[r][c] = self.steps  # 進入這格
                self.steps += 1  # 步數+1
                if self.steps == m*n: return True  # 成功走到

                if helper(r+2,c+1): return True  # 任一步成功，都可
                if helper(r+2,c-1): return True
                if helper(r+1,c+2): return True
                if helper(r+1,c-2): return True
                if helper(r-1,c+2): return True
                if helper(r-1,c-2): return True
                if helper(r-2,c+1): return True
                if helper(r-2,c-1): return True

                board[r][c] = -1  # 離開這格
                self.steps -= 1  # 步數-1
                return False  # 中間都沒成功離開，就是失敗
        
        helper(r,c)
        return board

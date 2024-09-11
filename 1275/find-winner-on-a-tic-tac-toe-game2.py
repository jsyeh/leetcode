# LeetCode 1275. Find Winner on a Tic Tac Toe Game
# 想模擬「井字遊戲」A,B 兩人依序下棋子 moves 有 i,j 值
# 如果有人win的話，就把名字回傳。如果下滿9子平手，就'Draw'
# 如果還沒下完，就 'Pending'
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['0']*3 for _ in range(3)]  # 棋盤先放 '0'
        name = ['A', 'B']  # 等下要依序放 'A' 或 'B'
        now = 0  # 0:'A', 1:'B' 要放在棋盤上
        for i,j in moves:
            board[i][j] = name[now]  # 把棋子放在棋盤上，再以 i,j 這個棋子，判斷「橫直斜斜」
            if board[i][0]==board[i][1]==board[i][2]: return name[now]
            if board[0][j]==board[1][j]==board[2][j]: return name[now]
            if i==j and board[0][0]==board[1][1]==board[2][2]: return name[now]
            if i+j==2 and board[0][2]==board[1][1]==board[2][0]: return name[now]

            # now = (now+1) % 2
            now = 1 - now  # 切換下棋的人
        if len(moves)==9: return 'Draw'  # 下完9子，平手
        else: return 'Pending'  # 沒有下完9子，還可再下

# 請問城堡rook「可以吃」幾個兵pawn
# 就反過來，查查看4個方向，會看到幾個兵pawn
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 先找出 Rook城堡的位置
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R": # 找到城堡了
                    rookI, rookJ = i, j
        # 題目保證「剛好有個城堡」所以別擔心
        dI = [1, 0,-1, 0] # 有4個攻擊的方向
        dJ = [0, 1, 0,-1]
        ans = 0
        for d in range(4): # 檢查4個方向
            i, j = rookI, rookJ # 初始位置
            while i>=0 and j>=0 and i<8 and j<8: # 還在合理的位置
                if board[i][j] == 'p': # 找到可以吃的兵了
                    ans += 1 # 找到一個答案
                    break # 離開這個方向的迴圈
                if board[i][j] == 'B': # 會卡住的主教
                    break # 離開這個方向的迴圈
                i, j = i+dI[d], j+dJ[d]
        return ans

# 有一堆 queens 座標，及1個 king座標，問「有哪些queens」可攻擊到king
# 註：橫的、直的、斜的，都能攻擊。但是被擋住的，就不能功擊。
# 所以應該「照著遠到進的距離」將queens排序，再依序檢查。
# 或是反過來觀察：king的8個方向，會先撞到哪些queens（要是先把 queens 放到 board）
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [[False]*8 for _ in range(8)]
        for i,j in queens:
            board[i][j] = True # 將 queens 放到 board
        ans = []
        dI = [ 1, 1, 1, 0,-1,-1,-1, 0] # 右下、下、左下、左、左上、上、右上、右
        dJ = [ 1, 0,-1,-1,-1, 0, 1, 1]
        for d in range(8): # 8個方向
            i, j = king # king 的座標
            while i>=0 and j>=0 and i<8 and j<8: # 還沒超過範圍
                if board[i][j]==True: # 有 queen 佔據
                    ans.append([i,j]) # 更新答案
                    break # 並離開這個方向的迴圈
                # 若無離開迴圈
                i, j = i+dI[d], j+dJ[d] # 往外走1步，以便下一輪迴圈再測
        return ans

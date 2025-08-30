# LeetCode 36. Valid Sudoku
# 「數獨」是 9x9 盤面，每行、每列、每方塊，都不能有重覆的數字
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper(i1, i2, j1, j2):  # 發明一個函式，在 i1...i2 及 j1...j2範圍內
            used = set()  # 把重覆的程式都放到函式裡，進行判斷
            for i in range(i1,i2):
                for j in range(j1,j2):
                    if board[i][j]=='.': continue
                    if board[i][j] in used: return False
                    used.add(board[i][j])
            return True
        for i in range(9):  # 橫列 row 逐列檢查有沒有重覆
            if helper(i, i+1, 0, 9) == False: return False
        for j in range(9):  # 直排 col 逐排檢查有沒有重覆
            if helper(0, 9, j, j+1) == False: return False
        for ii in range(3):  # 小正方塊 逐個檢查有沒有重覆
            for jj in range(3):  # 小正方塊 逐個檢查有沒有重覆
                if helper(ii*3, ii*3+3, jj*3, jj*3+3) == False: return False
        return True

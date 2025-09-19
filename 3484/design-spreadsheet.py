# LeetCode 3484. Design Spreadsheet
# 模擬「Excel試算表」的每一個格子處理：26個直行col
class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = [[0]*26 for i in range(rows+1)]
        # 建出很多 rows 每 row 有 26格，但因是 1-index 從1開始，所以「多開1格」

    def setCell(self, cell: str, value: int) -> None:
        X, Y = cell[0], int(cell[1:])  # 拆解出「英文」及「數字」
        self.rows[Y][ord(X)-ord('A')] = value  # 換算出「座標」並設定「值」

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)  # reset 就是設定「值」= 0

    def getCell(self, cell: str) -> int:  # 自己發明 getCell()函式
        if cell[0].isdigit(): return int(cell)  # 如果是數字開頭，即「數值」
        X, Y = cell[0], int(cell[1:])  # 不然就是「英文開頭」的「座標」
        return self.rows[Y][ord(X)-ord('A')]  # 換算出「座標」並取出「值」

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula[1:].split('+')  # 保證是 '=a+b' 的型式，所以切出來
        return self.getCell(cell1) + self.getCell(cell2)  # 用「自己發明 getCell()」來做事


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

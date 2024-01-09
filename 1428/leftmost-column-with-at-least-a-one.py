# row-sorted 表示每個 row 都是左邊0 右邊1
# 題目想問：最左邊的1在哪個col出現
# 有 BinaryMatrix 的 get() 與 dimensions()
# 真的很遜的話，也能暴力 get(i,j)全部查看
# 但不能呼叫超過1000次。後來看了 Editorial 有個很帥氣的解法，右上角開始，順著1及0來走
# 遇1往左試長度，遇0往下試新row。方法還蠻帥的。

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()
        # Editorial 的解法：右上角開始，遇1往左試長度，遇0往下試新row。方法還蠻帥的。
        i, j = 0, N-1 # 開始座標
        ansJ = -1
        while i<=M-1 and j>=0: # 合理的走動範圍
            if binaryMatrix.get(i,j)==1: # 遇1往左
                ansJ = j # 更新 col 為 ansJ 
                j -= 1 # 往左走，持續更析
            else: # 遇0往下再探
                i += 1
        return ansJ
        # 下面最笨的方法，就用暴力法，本以為100x100不大。但不能呼叫超過1000次
        # 在case 31/37 說，呼叫太多次.get()
        #for j in range(N):
        #    for i in range(M):
        #        if binaryMatrix.get(i,j)==1:
        #            return j # 找到 col j
        #return -1 # 沒有找到 1 就 return -1
# case 31/37: 因是 100x100 暴力法會呼叫超過1000次的題目上限，所以需要 binary search 法


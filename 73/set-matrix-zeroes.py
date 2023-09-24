# 陣列最大是200x200，如果裡面有0，就把對應的row,col都設成0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroI, zeroJ = [], []
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j]==0: # 遇到0時
                    zeroI.append(i) # 記錄對應的i
                    zeroJ.append(j) # 記錄對應的j

        for k in range(len(zeroI)): # 把記錄下來的i,j都逐一取出來
            i, j = zeroI[k], zeroJ[k]
            for ii in range(M): # 把整行 matrix[*][j] 全設為0
                matrix[ii][j]=0
            for jj in range(N): # 把整行 matrix[i][*] 全設為0
                matrix[i][jj]=0

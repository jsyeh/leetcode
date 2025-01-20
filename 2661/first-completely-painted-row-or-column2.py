# LeetCode 2661. First Completely Painted Row or Column
# 照著 arr[k] 的順序將mat對應格子著色，當k是多少時, 剛好將某條 row 或 col 全部著色
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        # 數字都不重覆，可用陣列「記錄對應的座標」，陣列從0開始，但題目從1開始，要多1格
        IJ = [(0,0)] * (M*N+1) # I,J 對照表：數字「對應」I,J座標。
        for i in range(M):
            for j in range(N):
                IJ[ mat[i][j] ] = (i,j) # 先做 i,j 對照表

        rows, cols = [0]*M, [0]*N  # 再建立 rows[i] 及 cols[j] 以便快速確認「是否集滿整條」
        for k,a in enumerate(arr):  # a = arr[k] 是現在處理的數字
            i, j = IJ[a] # 查回它對應的 i,j 座標
            rows[i] += 1 # 統計 row i 裡著色的次數
            cols[j] += 1 # 統計 col j 裡著色的次數
            if rows[i]==N or cols[j]==M: # 集滿整條
                # 小心看起來反過來，因為M個row, 每個row要集滿時,要N個
                return k # 找到了!

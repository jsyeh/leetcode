# 照著 arr[k] 的順序paint, k是多少時, 有第1個 row 或 col 全部著色
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        # 可以先建一個 dict, 以便快速找到 某個 arr[k] 對應的 (i,j) 
        # 再建立 rowSum[i] 及 colSum[j] 以便快速確認「是否集滿整條」
        IJ = {}
        for i in range(M):
            for j in range(N):
                IJ[ mat[i][j] ] = (i,j) # 先做 i,j 對照表
        
        rowSum = [0]*M
        colSum = [0]*N

        for k,a in enumerate(arr):
            i, j = IJ[a] # 查回它對應的 i,j 座標
            rowSum[i] += 1 # 統計本 row 出現次數
            colSum[j] += 1 # 統計本 col 出現次數
            if rowSum[i]==N or colSum[j]==M: # 集滿整條, 小心看起來反過來
                # 因為M個row, 每個row要集滿時,要N個
                return k # 找到了!
# case 460/1058: [1,4,5,2,6,3]
# [[4,3,5],
#  [1,2,6]]

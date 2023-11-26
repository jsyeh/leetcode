# 題目容易理解：matrix的col可左右調整，想問「最多1」的submatrix值 長方形面積
#   必須「全部都是1」我猜可能與 DP 有關。但我又沒有頭緒了。討論裡有人建議看答案
# 看了 Editorial 的第1段時，靈感就來了：  
# what is the area of a rectangle? It's B * H, where B is the base (width) and H is the height of the rectangle. As we are looking for the largest submatrix, we would prefer larger values for B and H.
#   也就是，照著高度來排序，便能知道「每一個寬度」對應的「高度」是多少。
#   但是，高度是多少呢？ Editorial 裡介紹很巧妙的作法，把連續的1持續加總
#   每個 row 都處理 sort 一次，看那個 row 裡，最多能「加到多少個方塊1」
# 再細看 Editorial 裡的圖解，有點感覺。

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        M, N = len(matrix), len(matrix[0])
        for i in range(M): # 希望一次處理整個row，後半才能排序
            for j in range(N):
                if i!=0 and matrix[i][j]==1: # 0 會 reset
                    # row[0]保留，其他都要算「上到下累積多少1」
                    matrix[i][j] = matrix[i-1][j] + 1 
            # 整個 row 處理完後
            thisRow = sorted(matrix[i], reverse=True) # 大排到小
            # print(thisRow) # 排完後，大的數字累積在左邊
            # 下面再針對「這個Row」能累積幾個「方塊1」
            for j in range(N):
                # 長方形公式，是寬(j+1)*高thisRow[j]，面積更大，就更新
                if thisRow[j]*(j+1)>ans: ans = thisRow[j]*(j+1)

        return ans

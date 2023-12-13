# 類似 8 Queen 問題，但簡化成 它的橫row 直col 都沒有其他的1
# 所以解法很簡單，看哪個 row 累積只有1個，哪個 col 累積只有1個，special
# 累計有幾個 special 的格子
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        rowSum = [0]*M
        colSum = [0]*N
        for i in range(M):
            for j in range(N):
                if mat[i][j]==1: # 若某格是1
                    rowSum[i] += 1 # 多1個1
                    colSum[j] += 1
        # ans1, ans2 = 0, 0
        # for i in range(M): # 如果在某個 row 總和是1，可能它有個speical
        #     if rowSum[i]==1: ans1 += 1
        # for j in range(N): # 如果在某個 col 總和是1，可能它有個speical
        #     if colSum[j]==1: ans2 += 1
        # return min(ans1, ans2) # 小的那個數，應該就是答案
        # 上面的方法，在 case 35/95 會出錯，所以還是要逐個1去查表檢查
        ans = 0
        for i in range(M):
            for j in range(N):
                if mat[i][j]==1 and rowSum[i]==1 and colSum[j]==1:
                    ans += 1
        return ans
# case 35/95: [
# [0,0,0,0,0,1,0,0],
# [0,0,0,0,1,0,0,1],
# [0,0,0,0,1,0,0,0],
# [1,0,0,0,1,0,0,0],
# [0,0,1,1,0,0,0,0]]

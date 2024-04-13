# 要找「最大的正方形」裡面全是1
# 本來想要用「積分圖」但好像還是太慢
# 看了 Editorial 的寫法，有介紹一種DP的圖示，想到方法
# 每個點用DP建表格，了解它1的左長、右長。
# 再每個點都測（對應「以它為最低點的答案」），往上長大
# 速度超慢的，因為它是 O(N^3)，沒有加速太多。
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        leftOne = [[0]*N for _ in range(M)]
        rightOne = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                leftOne[i][j] = int(matrix[i][j]) # 字串轉整數
                if leftOne[i][j]>0 and j>0: # 能往左長
                    leftOne[i][j] += leftOne[i][j-1]
            for j in range(N-1,-1,-1):
                rightOne[i][j] = int(matrix[i][j]) # 字串轉整數
                if rightOne[i][j]>0 and j<N-1: # 能往右長
                    rightOne[i][j] += rightOne[i][j+1]
        # 建好表格後，逐格找答案，用3層迴圈
        ans = 0 # 最大的面積
        for i in range(M):
            for j in range(N):
                # 挑個格子，以它為方塊的最低點，慢慢往上長大
                nowLeft, nowRight = leftOne[i][j], rightOne[i][j]
                nowArea = (1)*(nowLeft+nowRight-1) # 以i,j為底邊的目前面積
                for k in range(i-1, -1, -1): # 上界往上長大
                    nowLeft = min(nowLeft, leftOne[k][j]) # 可能會變小
                    nowRight = min(nowRight, rightOne[k][j]) # 可能會變小
                    nowArea = max(nowArea, (i-k+1)*(nowLeft+nowRight-1)) # 新的面積
                ans = max(ans, nowArea) # 答案面積更新
        return ans

# 以 rStart, cStart 為開始座標，右、下、左、 上 繞圈圈
# 超過範圍的就不用印，把範圍內的答案「i,j座標」逐一加到 ans 裡
# 顯然是模擬題
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        M, N = rows, cols # for i in range(M) vs. for j in range(N)
        dI = [0,1,0,-1] # 右下左上
        dJ = [1,0,-1,0] # 右下左上
        d = 0 # 0:右 1:下 2:左 3:上
        I, J = rStart, cStart # 現在的座標 在 開始點
        boundI = [inf,1,inf,-1] # I == cStart+boundI[d] 碰到邊界，便要移
        boundJ = [1,inf,-1,inf] # J == rStart+boundJ[d] 碰到邊界，便要移
        while len(ans)<M*N:
            if I>=0 and I<M and J>=0 and J<N: # 合理的範圍
                ans.append([I,J]) # 現在的座標要加入
            I += dI[d] # 前進一步
            J += dJ[d] # 前進一步
            if I == rStart+boundI[d] or J == cStart+boundJ[d]: # 碰到邊界
                boundI[d]+=dI[d] # 邊界外推
                boundJ[d]+=dJ[d] # 邊界外推
                d = (d+1)%4 # 改變方向
        return ans

        

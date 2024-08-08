# LeetCode 885. Spiral Matrix III 用螺旋的方式，繞過矩陣裡的每個數
# 這題是是模擬題，以 rStart, cStart 為開始座標，右、下、左、 上 繞圈圈
# 超過範圍的就不用印，把範圍內的答案「i,j座標」逐一加到 ans 裡
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        M, N = rows, cols # for i in range(M) vs. for j in range(N)
        d = 0 # 前進方向，對應 0:右 1:下 2:左 3:上
        dI = [0,1,0,-1]  # 前進的4個方向 右下左上，在i方向的移動量
        dJ = [1,0,-1,0]  # 前進的4個方向 右下左上，在j方向的移動量
        I, J = rStart, cStart  # 現在的座標 （一開始在開始點）
        ans.append([I,J])  # 把「現在的座標」加入
        for step in range(1,M+M+100):  # 要走的步閥「越來越大步」
            for p in range(2): # 每個步閥距離，要走2個方向：1右,1下,2左,2上,3右,3下,4左,4上
                for p2 in range(step):
                    I, J = I + dI[d], J+dJ[d]  # 前進一步，照著方向，走到下一格
                    if I>=0 and I<M and J>=0 and J<N:  # 合理的範圍
                        ans.append([I,J])  # 把「現在的座標」加入
                    if len(ans) == M*N: return ans  # 收齊全部資料，可以結束
                d = (d+1)%4  # 改變方向
        return ans

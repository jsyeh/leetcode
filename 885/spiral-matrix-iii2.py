# LeetCode 885. Spiral Matrix III 用螺旋的方式，繞過矩陣裡的每個數
# 這題是是模擬題，以 rStart, cStart 為開始座標，右、下、左、 上 繞圈圈
# 超過範圍的就不用印，把範圍內的答案「i,j座標」逐一加到 ans 裡
# 後來我又寫了一次，利用4個迴圈，對應4個方向，重覆的程式，好像比較容易理解。給大家參考。
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        I, J = rStart, cStart  # 現在的座標 （一開始在開始點）
        M, N = rows, cols
        ans = [[I,J]]  # 出發點
        step = 1
        while len(ans)<M*N:
            for j in range(step):  # 往右
                J += 1
                if I>=0 and I<M and J>=0 and J<N: ans.append([I,J])  # 現在的座標要加入
            for i in range(step):  # 往下
                I += 1
                if I>=0 and I<M and J>=0 and J<N: ans.append([I,J])  # 現在的座標要加入
            step += 1  # 每兩個方向，就再多走一步
            for j in range(step):  # 往左
                J -= 1
                if I>=0 and I<M and J>=0 and J<N: ans.append([I,J])  # 現在的座標要加入
            for i in range(step):  # 往上
                I -= 1
                if I>=0 and I<M and J>=0 and J<N: ans.append([I,J])  # 現在的座標要加入
            step += 1  # 每兩個方向，就再多走一步
        return ans

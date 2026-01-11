# LeetCode 85. Maximal Rectangle
# 想在 matrix 矩陣裡，找「標示'1'」的最大長方形
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])  # 長、寬
        histogram = [0] * (N+1)  # 橫向的 histogram 直方圖，累積到 row i 的高度H
        ans = 0
        for i in range(M):  # 針對 row i 計算對應的 histogram 直方圖
            for j in range(N):
                if matrix[i][j]=='1': histogram[j] += 1  # 累積高度「多1格」
                else: histogram[j] = 0  # 「高度」清為0
            
            # 接下來，利用 mono stack 從 histogram 找「到row i為止」最大的長方形
            stackJ, stackH = [-1], [0]  # 左邊放座標j，右邊放高度H，先塞值，讓迴圈容易寫
            for j in range(N+1):  # 多1格，會用到 histogram 最右邊的0來清空 stack 並更新最後1筆答案
                while stackH[-1] > histogram[j]:  # 更高的要吐掉
                    H = stackH.pop()  # 之前高度 H
                    stackJ.pop()  # 吐掉高度H對應的 j，寬度是再前一項 stackJ[-1] 的右邊開始
                    ans = max(ans, H * (j-stackJ[-1]-1))
                stackJ.append(j)
                stackH.append(histogram[j])
        return ans

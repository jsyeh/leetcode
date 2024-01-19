# 從上到下去，一開始可以是任一個位置，樓下則只能是左中右3選1，希望加總最小
# 就簡單的動態規劃即可。每個格子都有從樓上「到達它最小的值」
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        # 若想簡化memory用量，能回收使用 matrix[i][j]本身，來存DP的值
        for i in range(1,N): # 最上層不用做計算
            for j in range(N):
                smallest = matrix[i-1][j] # 樓上的最小值
                if j>0: smallest = min(smallest, matrix[i-1][j-1])
                if j<N-1: smallest = min(smallest, matrix[i-1][j+1])
                matrix[i][j] += smallest # 本身的值，加樓上「最小值」
        return min(matrix[N-1])

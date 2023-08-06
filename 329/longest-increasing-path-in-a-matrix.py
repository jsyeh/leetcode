# 329. Longest Increasing Path in a Matrix
# 感覺上 BFS 應該可以解決問題。最好再配上 Top-Down DP 可能會很棒。
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0]) # 得到matrix的高度M、寬度N
        table = [[0]*N for _ in range(M)] # 建出 Dynamic Programming 的表格
        # table[i][j] 表示i,j那一格開始的 Longest Increasing Path 長度

        def topDownDP(i, j) -> int: # Top-Down Dynamic Programming技巧
            if table[i][j]!=0: return table[i][j] # 之前有算過的話，快速得到答案
            # 去試4個方向
            a, b, c, d = 0, 0, 0, 0 # 4個方向鄰居格的答案
            if i-1>=0 and matrix[i-1][j] > matrix[i][j]: a = topDownDP(i-1, j)
            if i+1<M and matrix[i+1][j] > matrix[i][j]: b = topDownDP(i+1, j)
            if j-1>=0 and matrix[i][j-1] > matrix[i][j]: c = topDownDP(i, j-1)
            if j+1<N and matrix[i][j+1] > matrix[i][j]: d = topDownDP(i, j+1)

            table[i][j] = max(a,b,c,d) + 1 # 自己本身也算一格 （最差也能有1）
            return table[i][j]
        
        ans = 0
        for i in range(M):
            for j in range(N):
                now = topDownDP(i, j) # 每一格都算一次
                if now>ans: ans = now # 找最大值
        # print(table)
        return ans

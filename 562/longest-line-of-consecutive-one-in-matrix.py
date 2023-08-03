class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        table1 = [[0]*N for _ in range(M)] # table1[i][j]  橫
        table2 = [[0]*N for _ in range(M)] # table2[i][j]  直
        table3 = [[0]*N for _ in range(M)] # table3[i][j]  左上右下
        table4 = [[0]*N for _ in range(M)] # table4[i][j]  右上左下

        ans = 0
        for i in range(M):
            for j in range(N):
                if mat[i][j]==0: continue # 0就斷開了。
                # 下面則都是一
                table1[i][j] = table2[i][j] = table3[i][j] = table4[i][j] = 1
                if j>0: table1[i][j] += table1[i][j-1] # 橫的
                if i>0: table2[i][j] += table2[i-1][j] # 直的
                if i>0 and j>0: table3[i][j] += table3[i-1][j-1] # 左上右下
                if i>0 and j<N-1: table4[i][j] += table4[i-1][j+1] # 右上左下
                ans = max(ans, table1[i][j], table2[i][j], table3[i][j], table4[i][j])

        return ans


# 可以試試 high-level DP 的作法，最多走 maxMove, 步數會越來越少哦
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        table = [[[-1]*n for _ in range(m)] for _ in range(maxMove+1)]
        # table[s][i][j] 剩下s步時, grid[i][j] 能走到boundary外的paths數
        # 要 maxMove+1 是因為一開始會叫 helper(i, j, maxMove)
        def helper(i, j, move)->int:
            if move==0: return 0; # 步數走完，那就無路可走、別再走了
            print(i, j, move)
            if table[move][i][j]!=-1: return table[move][i][j] # 已算過可回傳

            a,b,c,d = 0,0,0,0 # 宣告4個變數，對應4個方向
            if i-1<0: a=1
            else: a = helper(i-1, j, move-1)
            if j-1<0: b=1
            else: b = helper(i, j-1, move-1)
            if i+1>=m: c=1
            else: c = helper(i+1, j, move-1)
            if j+1>=n: d=1
            else: d = helper(i, j+1, move-1)

            table[move][i][j] = (a+b+c+d) % 1000000007
            return table[move][i][j]
        
        return helper(startRow, startColumn, maxMove)
# case 81/94: 8 50 23 5 26 要小心，答案算出來會太大，所以要 % 1000000007
# case 85/94: 0 24 23 26 12 會超時，把 table[move][i][j] 初始值改成 -1 即可

# LeetCode 840. Magic Squares In Grid
# 3x3 的格子裡，1-9的數字剛好各出現1次，橫線、直線、對角線，加起來都是15
# 這樣的3x3格子，在 grid 裡有幾個呢？直接照著模擬，就可以完成了。
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i,j):  # 寫個函式，專門用來判斷「3x3格子，是否合規定」
            used = set()  # 每個數字都只出現一次
            for ii in range(i,i+3):  # 從 i,j 開始的 3x3 格子 grid[ii][jj]
                for jj in range(j,j+3):  # 必須介於1-9的數字，而不能重覆出現
                    if grid[ii][jj]<1 or grid[ii][jj]>9 or grid[ii][jj] in used:
                        return False  # 若不合格，就失敗
                    used.add(grid[ii][jj])  # 把每個數字 放入 set 裡，以便判斷是否重覆
            for ii in range(i,i+3):  # 橫的線
                now = 0
                for jj in range(j,j+3):
                    now += grid[ii][jj]  # 加起來是否剛好是 15
                if now!=15: return False  # 加起來是否剛好是 15
            for jj in range(j,j+3):  # 直的線
                now = 0
                for ii in range(i,i+3):
                    now += grid[ii][jj]  # 加起來是否剛好是 15
                if now!=15: return False  # 加起來是否剛好是 15
            if grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]!=15: return False  # 對角線
            if grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]!=15: return False  # 對角線
            return True
        M, N = len(grid), len(grid[0])
        ans = 0
        for i in range(M-2):  # 暴力試每一個可能的 3x3 格子
            for j in range(N-2):
                if isMagic(i,j): ans += 1
        return ans

# LeetCode 840. Magic Squares In Grid
# 3x3 的格子裡，1-9的數字剛好各出現1次，橫線、直線、對角線，加起來都是15
# 這樣的3x3格子，在 grid 裡有幾個呢？直接照著模擬，就可以完成了。
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        set9 = set(range(1,10))  # 1-9 數字都有出現
        def isMagic(i,j):  # 中心點在 (i,j)
            if grid[i][j] != 5: return False  # 正中心必須是5
            for ii,jj in (0,1),(1,1),(1,0),(1,-1):  # 右、右下、下、左下 將對應 左、左上、上、右上
                if grid[i-ii][j-jj] + grid[i+ii][j+jj] != 10: return False  # 對稱相加
            if grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] != 15: return False  # 上橫線
            if grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] != 15: return False  # 下橫線
            if grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] != 15: return False  # 左直線
            if grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] != 15: return False  # 右直線
            if set(grid[i-1][j-1:j+2]+grid[i][j-1:j+2]+grid[i+1][j-1:j+2])!=set9: 
                return False  # 1-9 數字都有出現
            return True  # 以上都沒壞掉，就是成功

        M, N = len(grid), len(grid[0])
        ans = 0
        for i in range(1,M-1):  # 暴力試每一個可能的 3x3 格子
            for j in range(1,N-1):
                if isMagic(i,j): ans += 1
        return ans


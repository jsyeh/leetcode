# 找出島(一堆1)的周長, 也就是繞一圈的長度。
# 想法很簡單: 從0變1、從1變0, 都是周長+=1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        M, N = len(grid), len(grid[0])
        for i in range(M): # 先看最左、最右的邊框
            if grid[i][0]==1: ans += 1 # 最左是否有陸地要算周長
            if grid[i][N-1]==1: ans += 1 # 最右
        for j in range(N): # 再看最上、最上的邊框
            if grid[0][j]==1: ans += 1 # 最上
            if grid[M-1][j]==1: ans += 1 # 最下
        print(ans)
        # 接著,看相鄰是否 0變1、1變0, 也就是兩格加起來為1
        for i in range(M-1): # 針對上下相鄰的每一格
            for j in range(N):
                if grid[i][j]+grid[i+1][j]==1: ans += 1 # 上下相鄰的部分
        for i in range(M): 
            for j in range(N-1): # 針對左右相鄰的每一格
                if grid[i][j]+grid[i][j+1]==1: ans += 1 # 左右相鄰的部分
        return ans

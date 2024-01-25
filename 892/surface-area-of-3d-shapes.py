# 在 nxn 的格子裡，放很多方塊，想算出「對應的表面積」
# 其實就是「上面」格子，加上「側面」兩個方向的最大值
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = N*N*2 # 先算「上面」頂樓及「下面」地板的面積
        # 但遇到 grid[i][j]==0時，要扣掉2個面積哦！

        # 兩個大樓的diff差，就會增加表面積
        for i in range(N): # 左手i 右手j 的方向、順序
            now = 0
            for j in range(N):                
                ans += abs(grid[i][j]-now)
                now = grid[i][j]
                # 但遇到 grid[i][j]==0時，要扣掉2個面積哦！
                if grid[i][j]==0: ans -= 2
            ans += now

        # 兩個大樓的diff差，就會增加表面積
        for j in range(N): # 另一個方向
            now = 0
            for i in range(N):
                ans += abs(grid[i][j]-now)
                now = grid[i][j]
            ans += now
        return ans

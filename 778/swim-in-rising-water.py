# LeetCode 778. Swim in Rising Water
# N x N 的格子，每個格子有「不同的數字」對應「水位」慢慢上升「哪一天上升會淹沒」
# 想問「第幾天」水淹沒的格子，能從左上角「游泳」到右下角
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [ (grid[0][0], 0, 0) ]  # 先把「起點」的 (高度,i,j) 放入 heap
        ans = grid[0][0]  # 起點的水位
        visited = set( [(0,0)] )  # 走過的點
        while heap:  # 利用 heap 把「小到大」依序加入 priority queue 裡 BFS
            h, i, j = heappop(heap)  # 目前路徑中，最低的高度
            ans = max(ans, h)  # 現在水位的高度
            if (i,j)==(N-1,N-1): return ans  # 順利走到 (N-1,N-1) 即可
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 往4方向試
                if ii<0 or jj<0 or ii>=N or jj>=N: continue  # 避開邊界外
                if (ii,jj) in visited: continue  # 避開走過的格子
                heappush(heap, (grid[ii][jj], ii, jj) )  # 加入 heap
                visited.add( (ii,jj) )  # 加入 set，避免之後重覆走

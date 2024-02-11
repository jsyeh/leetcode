# 本題 1463. Cherry Pickup II 與 741. Cherry Pickup 很像
# 我先用手機看了它們兩題的Editorial解釋，有點靈感，也照著寫看看。
# 想法有點像 3層的 DP，分別對應 r, c1, c2，對應機器人在 r,c1 和 r,c2 的位置

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # 先算出 rows x cols
        @cache
        def helper(r, c1, c2): # 機器人分別在 (r,c1) 和 (r,c2)
            if r>=M or c1<0 or c2<0 or c1>=N or c2>=N:
                return -inf # 不合理的走法，沒順利完成任務，是地雷走法，記「負無限大」
            if r==M-1 and c1>=0 and c2>=0 and c1<N and c2<N:
                if c1==c2: # 兩個走到同一格
                    return grid[r][c1] # 回傳1格的值
                else: # 兩個在不同格
                    return grid[r][c1] + grid[r][c2] # 2格的值加起來
            # 以上是DP的終止條件。以下則是「函式呼叫函式」
            # 從 Editorial 的寫法很巧妙，分別「左、中、右」3種狀況的最大值，各處理2個機器人
            below = max(helper(r+1,cc1,cc2) for cc1 in range(c1-1,c1+2) for cc2 in range(c2-1,c2+2))
            if c1==c2: # 兩個如果在同一格
                return grid[r][c1] + below
            else: # 兩個如果在不同格
                return grid[r][c1] + grid[r][c2] + below
        
        return helper(0,0,N-1) # 機器人在 (0,0) 及 (0,N-1) 一起開始往下走

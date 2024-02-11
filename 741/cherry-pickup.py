# 1463. Cherry Pickup II
# 本題 1463. Cherry Pickup II 與 741. Cherry Pickup 很像
# 我先用手機看了它們兩題的Editorial解釋，有點靈感，也照著寫看看。
# 想法有點像 3層的 DP。 1643 是用 r, c1, c2，對應機器人在 r,c1 和 r,c2 的位置
# 741 是用 r1,c1,c2，原因是r1+c1==r2+c2 都是對應走的步數，所以r2=r1+c1-c2
# 這題最酷的想法，本來是「一個機器人從0,0走到N-1,N-1，再走回0,0」的問題，
# 化簡成「兩個機器人，一起從0,0出發、走到N-1,N-1的位置」看「最多能收集多少」

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid) # 正方形的格子
        @cache
        def helper(r1,c1,c2):
            r2 = r1 + c1 - c2 # 機器人座標 r1,c1 和 r2,c2
            if r1<0 or r2<0 or c1<0 or c2<0: return -inf # 不合理的位置
            if r1>=N or r2>=N or c1>=N or c2>=N: return -inf # 不合理皫位置
            if grid[r1][c1]==-1 or grid[r2][c2]==-1: return -inf # 禁止的位置
            # 以上都是 return -inf 以避開走到這些位置
            # 兩個機器人都從 0,0 出發，要走到N-1,N-1
            if r1==N-1 and c1==N-1 and c2==N-1: # 走到目的地，當然r2也同時變N-1
                return grid[N-1][N-1] # 集合在最右下角的那一格，得到的分數
            # 接下來是「函式呼叫函式」的部分：有4種可能走法（向下、向右)*(向下、向右)
            # helper(向下、向下), helper(向下、向右), helper(向右、向下), helper(向右、向右)
            below = max(helper(r1+1,c1,c2),helper(r1+1,c1,c2+1),helper(r1,c1+1,c2), helper(r1,c1+1,c2+1))
            if c1==c2: # 因同個時間點「走的步數一樣」，所以c1==c2代表r1==r2在同一格
                return grid[r1][c1] + below # 現在在同一格
            else:
                return grid[r1][c1] + grid[r2][c2] + below # 現在在不同格
            
        ans = helper(0,0,0) # 兩個機器人，都從左上角一起出發
        if ans==-inf: return 0 # 如果是 -inf 代表沒有任何一種走法可行、走不到
        else: return ans

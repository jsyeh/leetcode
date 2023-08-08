# 先用暴力法試試吧 (結果暴力法超時)，暴力法500x500裡面有一堆0
# 後來發現有人分享另一種漂亮的爆力法， 500x500x(4*500) 的迴圈，把4個方向累積加起來
# https://leetcode.com/problems/bomb-enemy/solutions/83405/python-brute-force-o-mn-m-n-to-dp-o-mn/?envType=study-plan&envId=dynamic-programming-ii&plan=dynamic-programming
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        kills = [[0]*N for _ in range(M)]
        for i in range(M):
            row_hits = 0 # 往右巡
            for j in range(N):
                if grid[i][j]=='E': row_hits += 1
                elif grid[i][j]=='W': row_hits = 0
                else: kills[i][j] = row_hits
        for i in range(M):
            row_hits = 0 # 往左巡
            for j in reversed(range(N)):
                if grid[i][j]=='E': row_hits += 1
                elif grid[i][j]=='W': row_hits = 0
                else: kills[i][j] += row_hits
        for j in range(N):
            col_hits = 0 # 往下巡
            for i in range(M):
                if grid[i][j]=='E': col_hits += 1
                elif grid[i][j]=='W': col_hits = 0
                else: kills[i][j] += col_hits
        ans = 0 # 在最後一輪時，邊往上巡，邊更新答案 ans
        for j in range(N):
            col_hits = 0 # 往下巡
            for i in reversed(range(M)):
                if grid[i][j]=='E': col_hits += 1
                elif grid[i][j]=='W': col_hits = 0
                else: 
                    kills[i][j] += col_hits
                    if kills[i][j] > ans: ans = kills[i][j]
        return ans

# case 39/40: 一堆0


# LeetCode 3459. Length of Longest V-Shaped Diagonal Segment
# N x M 二維陣列裡，有0,1,2三種值。V-shape線段，是「從1出發」後續 2,0,2,0..
# 「走斜的方式」，最多「順時針」轉90度1次（也可以不轉），最長走多遠？
# 把「大問題變成小問題」很適合用 Dynamic Programming 來解
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # 地圖的長、寬
        di = [1,1,-1,-1]  # di,dj 分別對應 右下、左下、左上、右上
        dj = [1,-1,-1,1]  # 也就是當 d = (d+1)%4 時 di[d],dj[d] 會「順時針」轉動
        @cache  # 利用「函式呼叫函式」配合「cache記憶」來解決問題
        def helper(i, j, d, want, turned):  # 目前在i,j 方向d, 期待值want, 只能轉1次
            if i<0 or j<0 or i>=M or j>=N: return 0  # 撞出邊界、不能再走，距離是0
            if grid[i][j] != want: return 0  # 與期待值不同，失敗、斷開，距離是0
            # 不轉彎、轉彎，有兩種可能
            ans = helper(i+di[d], j+dj[d], d, 2-want, turned) + 1  # 答案會 + 1
            if turned < 1:  # 還可以轉彎
                d = (d+1) % 4  # 順時針轉
                ans2 = helper(i+di[d], j+dj[d], d, 2-want, turned+1) + 1 # 用掉1個彎
                ans = max(ans, ans2)
            return ans
        ans = 0
        for i in range(M):  # 測試所有的格子，如果是 1 就可以當「出發點」
            for j in range(N):
                if grid[i][j]==1:  # 可以當「出發點」
                    for d in range(4):  # 往4個方向探測
                        now = helper(i+di[d], j+dj[d], d, 2, 0) + 1 # 從i,j出發,方向d,期待2,已轉0次
                        ans = max(ans, now)  # 看這次探測結果，是否更好/值得更新
        return ans

# LeetCode 3197. Find the Minimum Area to Cover All Ones II
# grid 二維陣列，用「不重疊」的「3個長方形」把「全部的1」都「框起來」且「面積最小」
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def helper(i0,i1,j0,j1):  # LeetCode 3195 的上下左右界來解
            left, right = inf, -1  # 橫向的「左界、右界」
            up, down = inf, -1  # 直向的「上界、下界」
            for i in range(i0, i1):  # i0..i1 範圍內
                for j in range(j0, j1):  # j0..j1 範圍內
                    if grid[i][j]==1:  # 有1，就更新
                        left, right = min(left, i), max(right, i)
                        up, down = min(up, j), max(down, j)
            return (right-left+1) * (down-up+1)  # 算出「面積」
        M, N = len(grid), len(grid[0])  # 長、寬
        ans = inf
        # 「先用1條大線分、再分」共6種可能切法。暴力切出3塊後，暴力試過各種切法，「每塊」用 3195 的上下左右界來解
        for i in range(1, M):  # 橫切大刀，切出 big1上大塊 big2下大塊
            big1, big2 = helper(0, i, 0, N), helper(i, M, 0, N)
            for j in range(1,N):  # 直切小刀，切出 small1左小塊 small2右小塊
                small1, small2 = helper(0, i, 0, j), helper(0, i, j, N)  # 上面的左右2小塊
                ans = min(ans, big2 + small1 + small2)  # 下大塊 + 上面的左右2小塊
                small1, small2 = helper(i, M, 0, j), helper(i, M, j, N) # 下面的左右2小塊
                ans = min(ans, big1 + small1 + small2)  # 上大塊 + 下面的左右2小塊
            for i2 in range(i+1, M):  # 繼續橫切小刀，下方再切出 big2中塊 big2下塊
                big2, big3 = helper(i, i2, 0, N), helper(i2, M, 0, N)
                ans = min(ans, big1 + big2 + big3)  # 上大塊 + 中塊 + 下塊
        for j in range(1, N):  # 直切大刀，切出 big1左大塊 big2右大塊
            big1, big2 = helper(0, M, 0, j), helper(0, M, j, N)
            for i in range(1, M):  # 橫切小刀，切出 small1上小塊 small2下小塊
                small1, small2 = helper(0, i, 0, j), helper(i, M, 0, j)  # 左邊的上下2小塊
                ans = min(ans, big2 + small1 + small2)  # 右大塊 + 左邊的上下2小塊
                small1, small2 = helper(0, i, j, N), helper(i, M, j, N)  # 右邊的上下2小塊
                ans = min(ans, big1 + small1 + small2)  # 左大塊 + 右邊的上下2小塊
            for j2 in range(j+1, N):  # 繼續橫切小刀，右方再切出 big2中塊 big2右塊
                big2, big3 = helper(0, M, j, j2), helper(0, M, j2, N)
                ans = min(ans, big1 + big2 + big3)  # 左大塊 + 中塊 + 右塊
        return ans

# 有點像轉「魔術方塊」，有特別的「轉動一輪」的規則
# 先把 grid[i][j] 移到右邊 grid[i][j+1]
# 再把最右邊的 grid[i][n-1] 移到下一樓的 grid[i+1][0]
# 最右下角的 grid[m-1][n-1] 移到左上角 grid[0][0]
# 移動其實很花時間。其實就看 k 是多少，就照著「建出」ans 即可
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        # 往右移k，在重建時，其實就「往左查k格」
        ans = [[0]*N for _ in range(M)]
        for i in range(M*N):
            ii, jj = i//N, i%N # 從1D推算2D座標
            newI = (i-k+100*M*N)%(M*N) # 加大，避負數
            i0, j0 = newI//N, newI%N # 從1D推算2D座標
            # print(ii, jj, i0, j0) Debug 用
            ans[ii][jj] = grid[i0][j0]
        return ans
# case 5/107: [[1],[2],[3],[4],[7],[6],[5]] k=23
# 原來我把 %N 寫成 %M

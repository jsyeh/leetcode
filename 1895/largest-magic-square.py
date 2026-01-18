# LeetCode 1895. Largest Magic Square
# M x N 矩陣裡，找最大的 Magic Square (每個 row、每個col、對角線，加起來都相同)
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # 大矩陣的長、寬
        grid2 = list(zip(*grid))  # 「transpose轉置矩陣」，方便試每個col加總
        def checkSize(i,j,s):  # 這個函式確認 i,j開始、大小s的方塊，是否合格
            total = sum(grid[i][j:j+s])  # 「加起來要相同」的目標，挑row i
            for ii in range(i+1,i+s):  # 接下來試 row i+1 之後是否相同
                if total != sum(grid[ii][j:j+s]): return False  # 不同就失敗
            for jj in range(j,j+s):  # 接下來試 col j 之後是否相同
                if total != sum(grid2[jj][i:i+s]): return False  # 不同就失敗
            # 上面測試每條 row、每條col，下面是2條對角線
            if total != sum( [grid[i+k][j+k] for k in range(s)] ): return False
            if total != sum( [grid[i+k][j+s-1-k] for k in range(s)] ): return False
            return True  # 全部測試完、都沒失敗，就是成功
        def helper(s):  # 這個函式確認 size s 的矩陣，能不能成功
            for i in range(M-s+1):  # size s 的矩陣 所有可能的開始座標i
                for j in range(N-s+1):  # 開始座標j
                    if checkSize(i,j,s): return True  # 能成功
            return False  # 不能成功
        for s in range(min(M,N), 1, -1):  # 針對不同的大小
            if helper(s): return s  # 只要找到就是答案
        return 1  # 最基礎、一定成立的的答案是 1

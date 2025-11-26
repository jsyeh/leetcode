# LeetCode 2435. Paths in Matrix Whose Sum Is Divisible by K
# 從「左上」到「右下」有幾種走法（path加起來是k的倍數)
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])  # 方塊的長、寬
        MOD = 10**9+7  # 數字成長太大，要取餘
        @cache 
        def helper(i,j,mod):  # 到i,j這格「累積和」%k的餘數是mod
            if i>=M or j>=N: return 0  # 超過邊界
            mod = (mod+grid[i][j]) % k  # 走過現在這格，取 k 的餘數
            if i==M-1 and j==N-1:  # 走到「右下」終點
                if mod==0: return 1  # 這是一種合理的走法
                else: return 0  # 到最後時，mod不是0，無法被 k 整除
            return ( helper(i+1,j,mod) + helper(i,j+1, mod) ) % MOD
        ans = helper(0,0,0)  # 從0,0出發
        helper.cache_clear()
        return ans

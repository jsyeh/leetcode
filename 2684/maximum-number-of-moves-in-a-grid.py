# LeetCode 2684. Maximum Number of Moves in a Grid
# 從左到右走，能挑選「上、中、下」格，數字要越來越大，最多能走幾步？
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # 先得到長寬
        # table[i][j] 對應「能走到這格的長度」
        table = [[-1]*N for _ in range(M)]  # 建好表格，方便DP處理
        for i in range(M): table[i][0] = 0  # 0 代表可當出發點，-1代表還不能走
        ans = 0 
        for j in range(1,N):  # 從左到右，慢慢走
            for i in range(M):  # 上到下，每一層都要處理
                # 現在處理 table[i][j] 這格
                for k in range(max(0,i-1), min(i+2,M)):  # 來自「上、中、下」任1格
                    if grid[i][j] > grid[k][j-1] and table[k][j-1]!=-1:  # 更大，且有走過
                        table[i][j] = max(table[i][j], table[k][j-1]+1)  # 更新表格
                        ans = max(ans, table[i][j])  # 更新答案
        return ans

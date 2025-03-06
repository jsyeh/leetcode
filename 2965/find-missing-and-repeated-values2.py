# LeetCode 2965. Find Missing and Repeated Values
# N x N 矩陣裡，有 N平方 個數字，希望是 1...N平方
# 不過現在「有個數重覆」、「有個數漏掉」，請找出來。
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        ans = [0]*2
        total = 0  # 出現過的數，都加到 total 裡
        visited = set()  # 出現過的數
        for i in range(N):
            for j in range(N):
                if grid[i][j] in visited:  # 有出現過
                    ans[0] = grid[i][j]  # 就是重覆的數
                else:  # 沒出現過
                    total += grid[i][j]  # 加起來
                    visited.add(grid[i][j])  # 記下來
        ans[1] = (1+N*N)*N*N//2 - total
        # 1...N*N 總和 -「出現過的數的總和」得到「沒出現的那個數」
        return ans

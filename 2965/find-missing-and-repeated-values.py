# N*N 的matrix 共有N^2個數，本來希望1...N^2 都出現一次，但有個數出現2次，有個數沒出現
# 把它們兩個找出來。因為N<=50，可用暴力法
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        used = [0]*(N*N+1) # used[i] 統計 i 用了幾次

        for i in range(N):
            for j in range(N):
                used[grid[i][j]] += 1 # 用了1次
        ans = [-1,-1]
        for i in range(1,N*N+1):
            if used[i]==2: ans[0] = i
            if used[i]==0: ans[1] = i
        return ans

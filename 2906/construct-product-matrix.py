# 要把 matrix 裡，每個數字都乘起來。但不包含本身。
# 因數字太大，要 %12345
# 想到，可以把 matrix 做出「上半」「下半」「左條」「右條」
# 再逐一乘起來 %12345 即可
# 但再思考「左條」「右條」時，很難處理，因為要存好多不同的位置。
# 查看 Solutions 裡 stanistlav-iablokov 講到 flatten 變成1D
# 這時配合 prefix 及 suffix 即可，變更簡單。決定改用這個方法
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        prefix, suffix = [], []
        p, s = 1, 1 # prefix product vs. suffix proeuct
        for i in range(M):
            for j in range(N):
                p = p * grid[i][j] % 12345
                s = s * grid[M-1-i][N-1-j] %12345
                prefix.append(p) # 正著逐一乘起來
                suffix.append(s) # 反著逐一乘起來
        ans = [[1]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if i>0 or j>0: 
                    ans[i][j] *= prefix[i*N+j-1] # 前一項
                if i<M-1 or j<N-1: 
                    ans[i][j] *= suffix[M*N-1-(i*N+j+1)] # 後一項
                ans[i][j] %= 12345
        return ans

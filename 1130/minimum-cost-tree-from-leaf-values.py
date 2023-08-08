# 題目有點特別，non-leaf node 的值，是左右的 max 值存起來。所以要記下這個值 max
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)
        maxLeaf = [[0]*N for _ in range(N)]
        sumNonLeaf = [[0]*N for _ in range(N)]

        # 試試 bottom-up 的 DP 法
        
        for i in range(N): maxLeaf[i][i] = arr[i]

        for left in reversed(range(N)): # 倒過來的迴圈，讓右邊的小的都先建好
            sumNonLeaf[left][left] = 0

            for right in range(left+1, N):
                prev = maxLeaf[left+1][right] # 為因應倒過來，所以是往右看
                maxLeaf[left][right] = max(prev, arr[left])

                sumNonLeaf[left][right] = sumNonLeaf[left+1][right]
                sumNonLeaf[left][right] += maxLeaf[left][left] * maxLeaf[left+1][right]
                # 為因應倒過來，所以是加計 maxLeaf[left][left]

                for k in range(left+1, right):
                    sum = sumNonLeaf[left][k] + sumNonLeaf[k+1][right]
                    sum += maxLeaf[left][k] * maxLeaf[k+1][right]
                    if sum < sumNonLeaf[left][right]:
                        sumNonLeaf[left][right] = sum
        
        return sumNonLeaf[0][N-1]



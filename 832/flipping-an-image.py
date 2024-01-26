# 先「左右」flip，再把 0<->1 互換
# 其實就用 for 迴圈調整左右，再 1-image[i][j] 即可
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        M, N = len(image), len(image[0])
        ans = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                ans[i][j] = 1-image[i][N-1-j]
        return ans

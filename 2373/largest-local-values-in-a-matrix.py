# LeetCode 2373. Largest Local Values in a Matrix
# 久違的 Easy 題，只要會 for 迴圈 和 陣列，就能寫了，開心！
# 在 n x n 的 grid[i][j] 想在它附近找到 3 x 3 的小格子，算出裡面最大值
# 因為 n 最大是 100， 所以 100 x 100 算出來的答案最大是 98 x 98
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)  # 先知道正方型的邊長 N
        N2 = N - 2  # 答案的正方型的邊長 N2
        ans = [[0] * N2 for i in range(N2)]  # 這是 Python 產生二維陣列的作法
        for i in range(N - 2):
            for j in range(N - 2):
                # 針對每個 grid[i][j], 找到它附近的 3 x 3 的格子
                local = 0  # 想找 local 的最大值，一開始是0
                for ii in range(3):  # i + ii 是想探索的範圍
                    for jj in range(3):  # j + jj 是想探索的範圍
                        # 在探索的範圍內，找 local 的最大值
                        local = max(local, grid[i + ii][j + jj])
                ans[i][j] = local  # 把 local 最大值，放入 ans[i][j] 裡
        return ans

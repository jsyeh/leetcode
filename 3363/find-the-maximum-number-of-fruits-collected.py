# LeetCode 3363. Find the Maximum Number of Fruits Collected
# n x n 格子/房間裡，fruits[i][j] 對應「房間(i,j)有多少水果」
# 3 個小孩的開始位置在 左上(0,0)、右上(0,n-1)、左下(n-1,0)，皆需移動 n-1 步「到右下」
# 每次有三種相鄰的可能走法，最多能收多少水果？Hint 說「對角線」一定會走直線
# 另兩個小孩則用 dynamics programming 即可
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        ans = sum([fruits[i][i] for i in range(N)])  # 對角線的和
        for i in range(N-1):
            for j in range(N-i-1):
                fruits[i][j] = 0  # 清左上角的三角形，因左下角、右下角的2個小孩都走不到
        for i in range(1,N):
            for j in range(i,N):
                if j==N-1: fruits[i][j] += max(fruits[i-1][j-1], fruits[i-1][j])
                else: fruits[i][j] += max(fruits[i-1][j-1], fruits[i-1][j], fruits[i-1][j+1])

        for j in range(1,N):
            for i in range(j,N):
                if i==N-1: fruits[i][j] += max(fruits[i-1][j-1], fruits[i][j-1])
                else: fruits[i][j] += max(fruits[i-1][j-1], fruits[i][j-1], fruits[i+1][j-1])
        return ans + fruits[-1][-2] + fruits[-2][-1]

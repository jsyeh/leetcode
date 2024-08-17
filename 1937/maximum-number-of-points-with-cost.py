# LeetCode 1937. Maximum Number of Points with Cost
# 在 matrix 裡，從上到下「每個row」挑1個數 points[i][j] 得分
# 但移動要付出「移動距離」的代價，你能從 matrix 裡，得到多少點數？
# 用 DP 來解：每個格子，都會對應「從上到下」到它時，最多的點數
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        M, N = len(points), len(points[0])
        for i in range(1,M):
            # 本來直覺想到「先2個迴圈i,j」再「1個迴圈k」的作法 O(n^3) 太慢
            # 可利用 LeetCode 121 及 1014 的技巧，減少1層迴圈   
            left, right = [0]*N, [0]*N  # 用 left[k], right[k] 事先算一次
            left[0] = points[i-1][0]  # 樓上累積的最佳點數（從左數過來）
            for k in range(1,N):  # left[k] 對應「樓上左邊數到k」最好的結果
                left[k] =max(left[k-1]-1, points[i-1][k])
            right[-1] = points[i-1][-1]  # 樓上累積的最佳點數（從右數過來）
            for k in range(N-2,-1,-1):  # right[k] 對應「數上右邊數到k」最好的結果
                right[k] = max(right[k+1]-1, points[i-1][k])

            for j in range(N):
                points[i][j] += max(left[j], right[j])  # 兩個方向的最佳的那個結果
        return max(points[M-1][:])  # 最後一層的最大值
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        # 本來直覺想到「先2個迴圈i,j」再「1個迴圈k」的作法 O(n^3) 太慢
        # 在 case 141/157 有大量數字 10^5 會「超時」
        # 可利用 LeetCode 121 及 1014 的技巧，減少1個迴圈
        for i in range(1,M):  # row 0 的部分不用動
            for j in range(N):  # 直接在 points[i][j]更新答案
                best = 0
                for k in range(N): # 決定樓上 i-1 層的位置
                    best = max(best, points[i-1][k]+points[i][j]-abs(k-j))
                points[i][j] = best
        return max(points[M-1][:])
'''

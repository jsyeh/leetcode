# 有很多條 arrays 各自排序好, 在不同條中，挑2條的2個數，距離最大
# 其實一定就是「挑」每條的最小、最大的兩個數。再去比。
# 但是，又不能找最大、最小值相減，因它們在同一條就不行。
# 想到可以簡單的「DP」來解：前面i條的最大最小，若第i+1條，有更好嗎？
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0 # 最大的距離
        N = len(arrays)
        m, M = arrays[0][0], arrays[0][-1] # 最小值、最大值
        for i in range(1, N):
            # 更新可能的「最大距離」
            ans = max(ans, M - arrays[i][0], arrays[i][-1] - m)
            # 這回合比較完後，更新最小值m，最大值M
            m = min(m, arrays[i][0]) 
            M = max(M, arrays[i][-1])
        return ans

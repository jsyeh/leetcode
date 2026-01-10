# LeetCode 547. Number of Provinces
# matrix isConnected 裡，有些是相連的。有幾個 connected component?
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        visited = set()
        N = len(isConnected)
        def dfs(i):
            visited.add(i)
            for k in range(N):
                if isConnected[i][k] and k not in visited:
                    dfs(k)
        for i in range(N):
            if i not in visited:
                ans += 1
                dfs(i)
        return ans

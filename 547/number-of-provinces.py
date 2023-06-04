class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        print(N)
        visited = list((False,)*N)
        ans = 0
        def visiting(i):
            visited[i] = True
            for k in range(N):
                if isConnected[i][k] and not visited[k]:
                    visiting(k)
        for i in range(N):
            if not visited[i]:
                ans += 1
                visiting(i)
        return ans



class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N = len(costs)
        K = len(costs[0])
        table = [([0]*K) for _ in range(N)]
        for k in range(K):
            table[0][k] = costs[0][k]
        
        for i in range(1,N):
            for k in range(K):
                prevCost = 999999999
                for kk in range(K):
                    if kk!=k and table[i-1][kk]<prevCost:
                        prevCost = table[i-1][kk]
                table[i][k] = costs[i][k] + prevCost;
        print(table)
        ans = table[N-1][0]
        for k in range(1,K):
            if table[N-1][k] < ans:
                ans = table[N-1][k]
        return ans

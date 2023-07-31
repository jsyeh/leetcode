class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        table = [0]*(N+1)
        table[0] = 0 # 第0步，總cost是0
        table[1] = cost[0] # 第1步，總cost是踩在cost[0]
        for i in range(2,N+1):
            table[i] = cost[i-1] + min(table[i-1], table[i-2])
        
        return min(table[N], table[N-1])


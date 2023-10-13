class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # You can either start from the step with index 0, or the step with index 1.
        # 所以一開始可以站在 cost[0] 或 cost[1]
        N = len(cost)
        ans = [inf]*(N+1)
        # Once you pay the cost, you can either climb one or two steps.
        # 意思是，站在上面不用錢，是要再往上時要錢
        ans[0] = 0 # 一開始可以站在0所以不用錢
        ans[1] = 0
        for i in range(2,N+1):
            ans[i] = min(ans[i-1]+cost[i-1], ans[i-2]+cost[i-2])
        print(ans)
        return ans[N]
        

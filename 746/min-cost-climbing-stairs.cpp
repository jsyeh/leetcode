class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int N = cost.size();
        int ans[N+2];
        ans[0] = 0;
        ans[1] = cost[0];
        for(int i=2; i<=N; i++){
            ans[i] = cost[i-1] + min(ans[i-1], ans[i-2]);
//printf("%d ", ans[i]);
        }
        return min(ans[N], ans[N-1]);
    }
};

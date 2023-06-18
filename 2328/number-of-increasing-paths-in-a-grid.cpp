//這題我也沒什麼頭緒，所以查看 Solutions 裡的解法
//https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/solutions/2229819/c-python-top-down-dp/
//裡面的重點，是4個方向，都去試，查看 dp 的結果，再加起來
class Solution {
public:
    vector<vector<long long int>> memo; //好像 Top-down DP 起手勢，都有memo 存（問過的）答案
    int M, N, MOD=1000000007;
    int countPaths(vector<vector<int>>& grid) {
        long long int ans = 0;
        M = grid.size();
        N = grid[0].size();
        memo.resize(M, vector<long long int>(N, -1)); //初始值都設-1表示還沒來過
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                int t = dp(grid, i, j, INT_MIN);
                ans = (ans + t) % MOD;
//printf("%lld(%d) ", memo[i][j], t);
            }
//printf("\n");
        }
        return ans;
    }

    long long int dp(vector<vector<int>>& grid, int i, int j, int prev) {
        if(i<0 || j<0 || i>=M || j>=N) return 0;//不合理的走法
        if(grid[i][j]<=prev) return 0; //沒有嚴格遞增，就不是合理的走法
        //這裡的順序有差，要先把「需排除」的return 0 之後才能查memo[i][j]值
        if(memo[i][j]!=-1) return memo[i][j]; //之前有查過答案

        prev = grid[i][j];
        long long int ans = 1; //有進來，就是一種解法
        
        ans = (ans + dp(grid, i+1, j, prev)) % MOD;
        ans = (ans + dp(grid, i-1, j, prev)) % MOD;
        ans = (ans + dp(grid, i, j+1, prev)) % MOD;
        ans = (ans + dp(grid, i, j-1, prev)) % MOD;

        return memo[i][j] = ans; //記下這次的答案
    }
};
//case 34/36: 有大量的資料，所以超時
//因為我忘了 memo[i][j] = ans 所以沒有加速，

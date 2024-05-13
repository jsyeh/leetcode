class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        for(int i=0; i<M; i++) { //針對每個 row 最高位的 grid[i][0]
            if(grid[i][0]==0) { // 整個 row i 要 flip
                for(int j=0; j<N; j++) {
                    grid[i][j] = 1 - grid[i][j]; // 用減法，可將0,1對調
                }
            }
        }
        int ans = M;
        for(int j=1; j<N; j++) { //從次高位，到最右邊的位數
            int now = 0; 
            for(int i=0; i<M; i++) { // 直col逐個處理
                now += grid[i][j]; // 統計有幾個1
            }
            ans = ans * 2 + max(now, M-now); // 再把答案累積
        }
        return ans;
    }
};

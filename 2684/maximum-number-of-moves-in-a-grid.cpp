// LeetCode 2684. Maximum Number of Moves in a Grid
// 動態規劃題：從最左邊出發，往右上/右/右下走「步步高昇」越走越高，最多走幾步
class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        bool visited[M][N];  // 可以走到的點
        for(int i=0; i<M; i++) {
            visited[i][0] = true;  // 最左邊可走
            for(int j=1; j<N; j++) visited[i][j] = false; // 其他格，都先填 false
        }
        // 上面初始值，下面開始 DP走動測試
        for(int j=1; j<N; j++) { // 右邊1格開始，往前回顧
            bool goHere = false; // 現在能走到第j個 column 嗎？
            if((visited[0][j-1] && grid[0][j]>grid[0][j-1]) || (visited[1][j-1] && grid[0][j]>grid[1][j-1])) {
                visited[0][j] = true; // 最上面 [0][j] 可走
                goHere = true; // 有走到j
            }
            for(int i=1; i<M-1; i++) { // 每格都檢查
                for(int ii=i-1; ii<=i+1; ii++) { // 右上、右、右下，都檢查
                    if(visited[ii][j-1] && grid[i][j]>grid[ii][j-1]) {
                        visited[i][j] = true; // [i][j] 可走
                        goHere = true; // 有走到j
                    }
                }
            }
            if((visited[M-1][j-1] && grid[M-1][j]>grid[M-1][j-1]) || (visited[M-2][j-1] && grid[M-1][j]>grid[M-2][j-1])) {
                visited[M-1][j] = true; // 最下面 [M-1][j] 可走
                goHere = true; // 有走到j
            }
            if(!goHere) {
                return j-1; // 最後若沒能走到j,就只能走到j-1而已
            }
        }
        return N-1; // 能走到最後，那就是走 N-1 步
    }
};

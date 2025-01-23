// LeetCode 1267. Count Servers that Communicate
// 地圖 grid[i][j] 裡 1:有電腦，0:沒有電腦，兩台電腦在同一直線or橫線「可互連」。
int countServers(int** grid, int gridSize, int* gridColSize) {
    int M = gridSize, N = gridColSize[0];
    int rows[M], cols[N], total = 0; // 問「有幾台電腦」可連到其他台電腦？
    for(int i=0; i<M; i++) rows[i] = 0;
    for(int j=0; j<N; j++) cols[j] = 0;
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            if(grid[i][j]==1) { // 先統計電腦在哪裡
                rows[i]++; // 第 i row 多1台電腦
                cols[j]++; // 第 j row 多1台電腦
                total++; // 電腦的總數
            }
        }
    }
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            if(grid[i][j]==1 && rows[i]==1 && cols[j]==1) {
                total--; // 遇到落單的電腦，扣掉它
            }
        }
    }
    return total; // 最後留著的電腦，都有同伴「可互連」
}

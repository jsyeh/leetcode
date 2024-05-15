// LeetCode 1219. Path with Maximum Gold
// 金礦 grid[i][j] 有不同數量的 gold 可開採, 可從任意地方開始, 一格格開採
// 不能走到 gold為0的格子。問最多能得到多少金礦。看起來用 DFS 就可以解決了。
int max(int a, int b) {
    if(a>b) return a;
    else return b;
} // 在 C 語言裡, 2D 陣列會用2顆指標 來實作 (這個例子參數傳比較多)
int dfs(int** grid, int i, int j, int M, int N) {
    if(i<0 || j<0 || i>=M || j>=N) return 0; // 超過邊界
    if(grid[i][j]==0) return 0; // 走過 or 不能走到 0 的格子
    int gold_here = grid[i][j]; // 這格有 gold_here 的金礦可採
    grid[i][j] = 0; //暫清為0, 稍後不能進來
    int ans1 = dfs(grid, i+1, j, M, N); // 往4個方向, 都試過一次
    int ans2 = dfs(grid, i-1, j, M, N);
    int ans3 = dfs(grid, i, j+1, M, N);
    int ans4 = dfs(grid, i, j-1, M, N);
    grid[i][j] = gold_here; // 離開時, 把 gold 放回去
    return gold_here + max(max(ans1,ans2), max(ans3,ans4)); // 用最大值
}
int getMaximumGold(int** grid, int gridSize, int* gridColSize) {
    int M = gridSize, N = gridColSize[0];
    int ans = 0;
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            ans = max(ans, dfs(grid, i, j, M, N));
        }
    }
    return ans;
}

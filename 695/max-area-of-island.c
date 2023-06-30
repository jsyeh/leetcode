int helper(int** grid, int M, int N, int i, int j) {
    if(i<0 || j<0 || i>=M || j>=N) return 0;

    if(grid[i][j]==0) return 0;
    else grid[i][j] = 0;

    int ans = 1;
    ans += helper(grid, M, N, i+1, j);
    ans += helper(grid, M, N, i-1, j);
    ans += helper(grid, M, N, i, j+1);
    ans += helper(grid, M, N, i, j-1);
    return ans;
}
int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){
    int M = gridSize, N = gridColSize[0];
    int ans = 0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]!=0){
                int temp = helper(grid, M, N, i, j);
                if(temp>ans) ans = temp;
            }
        }
    }
    return ans;
}

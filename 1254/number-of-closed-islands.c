void helper(int** grid, int M, int N, int i, int j){
    if(i<0 || j<0 || i>=M || j>=N) return;

    if(grid[i][j]==1) return;

    grid[i][j] = 1;
    helper(grid, M, N, i+1, j);
    helper(grid, M, N, i-1, j);
    helper(grid, M, N, i, j+1);
    helper(grid, M, N, i, j-1);
}
int closedIsland(int** grid, int gridSize, int* gridColSize){
    int M = gridSize, N = gridColSize[0];
    for(int i=0; i<M; i++){
        helper(grid, M, N, i, 0);
        helper(grid, M, N, i, N-1);
    }
    for(int j=0; j<N; j++){
        helper(grid, M, N, 0, j);
        helper(grid, M, N, M-1, j);
    }

    int ans = 0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]==0){
                ans++;
                helper(grid, M, N, i, j);
            }
        }
    }
    return ans;
}

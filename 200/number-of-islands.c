int M, N;
int numIslands(char** grid, int gridSize, int* gridColSize){
    M = gridSize;
    N = gridColSize[0];

    int ans=0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]=='1'){
                printf("Yes");
                ans++;
                travel(grid, i, j);
            }
        }
    }
    return ans;
}
void travel(char** grid, int i, int j) {
    if(i<0 || j<0 || i>=M || j>=N) return;
    if(grid[i][j]=='0') return;
    grid[i][j] = '0';
    travel(grid, i-1, j);
    travel(grid, i+1, j);
    travel(grid, i, j-1);
    travel(grid, i, j+1);
}

int M, N;
int fresh(int** grid){
    int ans=0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]==1) ans++;
        }
    }
    return ans;
}

int neighborRotting(int** grid, int i, int j){
    if(i-1>=0 && grid[i-1][j]==2) return 2;
    if(j-1>=0 && grid[i][j-1]==2) return 2;
    if(i+1<M && grid[i+1][j]==2) return 2;
    if(j+1<N && grid[i][j+1]==2) return 2;
    return 1;
}

void rotting(int** grid1, int ** grid2){
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid1[i][j]==0)  grid2[i][j] = 0;
            else if(grid1[i][j]==2) grid2[i][j] = 2;
            else {
                grid2[i][j] = neighborRotting(grid1, i, j);
            }
        }
    }
}

int orangesRotting(int** grid, int gridSize, int* gridColSize){
    M = gridSize;
    N = gridColSize[0];
    int** grid1 = grid;
    int** grid2 = (int**)malloc(sizeof(int*)*M);
    for(int i=0; i<M; i++) grid2[i] = (int*)malloc(sizeof(int)*N);

    int prevFresh = fresh(grid);
    if(prevFresh==0) return 0;

    for(int i=1;  ; i++){
        rotting(grid1, grid2);
        int nextFresh = fresh(grid2);
        if(nextFresh==0) return i;
        if(nextFresh==prevFresh) return -1;
        prevFresh = nextFresh;
        int** temp = grid1;
        grid1 = grid2;
        grid2 = temp;
    }
    return 0;
}

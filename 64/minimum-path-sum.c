int minPathSum(int** grid, int gridSize, int* gridColSize){
    int M = gridSize, N = gridColSize[0];
    int table[M][N];
    table[0][0] = grid[0][0];
    for(int i=1; i<M; i++){
        table[i][0] = table[i-1][0] + grid[i][0];
    }
    for(int j=1; j<N; j++){
        table[0][j] = table[0][j-1] + grid[0][j];
    }

    for(int i=1; i<M; i++){
        for(int j=1; j<N; j++){
            table[i][j] = grid[i][j];
            if(table[i-1][j]<table[i][j-1]) table[i][j] += table[i-1][j];
            else table[i][j] += table[i][j-1];
        }
    }
    return table[M-1][N-1];
}

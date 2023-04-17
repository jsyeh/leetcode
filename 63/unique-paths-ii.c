int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    int M = obstacleGridSize, N = *obstacleGridColSize;
    int table[101][101];
    
    table[0][0] = 1;
    for(int i=0; i<M; i++) {
        if(obstacleGrid[i][0]==1) table[i][0] = 0;
        else if(i>0) table[i][0] = table[i-1][0];
        
        for(int j=1; j<N; j++){
            table[i][j]=0;
            if(obstacleGrid[i][j]==1) continue;
            
            if(i!=0) table[i][j] += table[i-1][j];
            table[i][j] += table[i][j-1];
        }
    }
    return table[M-1][N-1];
}

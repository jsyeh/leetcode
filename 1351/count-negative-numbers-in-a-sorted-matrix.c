int countNegatives(int** grid, int gridSize, int* gridColSize){
    int ans = 0;
    for(int i=0; i<gridSize; i++){
        for(int j=0; j<gridColSize[0]; j++){
            if( grid[i][j] < 0 ) ans++;
        }
    }
    return ans;
}

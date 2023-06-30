void DFS(int** grid, int M, int N, int i, int j, int ID){
    if(i<0 || j<0 || i>=M || j>=N) return;
    if(grid[i][j]==1){
        grid[i][j] = ID;
        DFS(grid, M, N, i+1, j, ID);
        DFS(grid, M, N, i-1, j, ID);
        DFS(grid, M, N, i, j+1, ID);
        DFS(grid, M, N, i, j-1, ID);
    }
}

bool DFS2(int** grid, int M, int N, int i, int j, int ID2, int** grid1, int ID1){
    if(i<0 || j<0 || i>=M || j>=N) return true; //沒事，不算錯誤，只是不做事
    bool bad = false;
    if(grid[i][j]==1){
        if(ID1 != grid1[i][j]) return false;//不在同一個ID1,就是錯誤
        grid[i][j] = ID2;
        //若提早結束時，可能有些land就沒有走到
        if(!DFS2(grid, M, N, i+1, j, ID2, grid1, ID1)) bad = true;//沒通過檢測，false (not good)
        if(!DFS2(grid, M, N, i-1, j, ID2, grid1, ID1)) bad = true;;
        if(!DFS2(grid, M, N, i, j+1, ID2, grid1, ID1)) bad = true;;
        if(!DFS2(grid, M, N, i, j-1, ID2, grid1, ID1)) bad = true;;
    }
    if(bad) return false;
    return true;//順利經過檢測，就是true (good)
}

void showGrid(int** grid, int M, int N){
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize){
    int M = grid1Size, N = grid1ColSize[0];
    //int M2 = grid2Size, N2 = grid2ColSize[0]; 兩個地圖一樣長寬，所以不用再宣告
    int ID=2;//從2開始數
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid1[i][j]==1){
                DFS(grid1, M, N, i, j, ID++);
            }
        }
    }
    //showGrid(grid1, M, N);

    int ans = 0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid2[i][j]==1 && grid1[i][j]!=0){
                bool good = DFS2(grid2, M, N, i, j, ID++, grid1, grid1[i][j]);
                if(good) ans++;
            }
        }
    }
    //printf("---\n");
    //showGrid(grid2, M, N);
    //printf("---\n");
    return ans;
}

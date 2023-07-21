int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize){
    int M = matrixSize, N = matrixColSize[0];
    //想法：從下往上建構，所以迴圈要反過來
    int table[M][N]; //table[i][j] 表示 matrix[i][j]往下走的各種走法，最小的值

    for(int j=0; j<N; j++){
        table[M-1][j] = matrix[M-1][j];
    }
    for(int i=M-2; i>=0; i--){
        for(int j=0; j<N; j++){
            int small = table[i+1][j];
            if(j-1>=0 && table[i+1][j-1]<small) small = table[i+1][j-1];
            if(j+1<N && table[i+1][j+1]<small) small = table[i+1][j+1];

            table[i][j] = matrix[i][j] + small;
        }
    }
    int ans = INT_MAX;
    for(int j=0; j<N; j++){
        if(table[0][j]<ans) ans = table[0][j];
    }
    return ans;
}

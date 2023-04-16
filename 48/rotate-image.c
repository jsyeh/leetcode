void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int N = matrixSize;
    *matrixColSize = N;

    for(int i=0; i<matrixSize/2; i++){
        for(int j=0; j<(matrixSize+1)/2; j++){
            int temp=matrix[i][j];
            matrix[i][j] = matrix[N-1-j][i];
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j];
            matrix[N-1-i][N-1-j] = matrix[j][N-1-i];
            matrix[j][N-1-i] = temp;
        }
    }
}

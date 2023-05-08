int diagonalSum(int** mat, int matSize, int* matColSize){
    int M = matSize, N = matColSize[0];

    int sum = 0;
    for(int i=0; i<M; i++){
        sum += mat[i][i];
        if(i!=M-1-i) sum += mat[M-1-i][i];
    }
    return sum;
}

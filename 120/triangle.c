//倒過來的方法，從下到上來找到結果
int min(int a, int b){
    if(a<b) return a;
    return b;
}
int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
    int M = triangleSize;
    int table[M][M];
    for(int j=0; j<M; j++){
        table[M-1][j] = triangle[M-1][j];
    } //先把底層的值放好

    for(int i=M-2; i>=0; i--){
        for(int j=0; j<triangleColSize[i]; j++){
            table[i][j] = min(table[i+1][j], table[i+1][j+1]) + triangle[i][j];
        }
    }
    return table[0][0];
}

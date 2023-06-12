/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes){
    int M = matSize, N = matColSize[0];
    int Qi[M*N+1], Qj[M*N+1];
    int front = 0, back = 0, Qn=0;
    int a[M+2][N+2]; //visited 1 will become 0
    for(int i=0; i<M+2; i++){ //邊界是哨兵
        for(int j=0; j<N+2; j++){ //邊界是哨兵
            if(i==0 || j==0 || i==M+1 || j==N+1) a[i][j] = 0;
            else a[i][j] = mat[i-1][j-1];
        }
    }
    for(int i=1; i<=M; i++){
        for(int j=1; j<=N; j++){
            if(a[i][j]==0){
                Qi[back] = i;
                Qj[back] = j;
                back++;
                Qn++;
            }
        }
    }
    while(Qn>0){
        int i = Qi[front], j = Qj[front], now = mat[i-1][j-1];
        front++;
        Qn--;
        if(a[i-1][j]==1){
            a[i-1][j]=0;
            Qi[back]=i-1;
            Qj[back]=j;
            mat[i-2][j-1]=now+1;
            back++;
            Qn++;
        }
        if(a[i+1][j]==1){
            a[i+1][j]=0;
            Qi[back]=i+1;
            Qj[back]=j;
            mat[i][j-1]=now+1;
            back++;
            Qn++;
        }
        if(a[i][j-1]==1){
            a[i][j-1]=0;
            Qi[back]=i;
            Qj[back]=j-1;
            mat[i-1][j-2]=now+1;
            back++;
            Qn++;
        }
        if(a[i][j+1]==1){
            a[i][j+1]=0;
            Qi[back]=i;
            Qj[back]=j+1;
            mat[i-1][j]=now+1;
            back++;
            Qn++;
        }
    }



    *returnSize = matSize;
    *returnColumnSizes = (int*)malloc(sizeof(int)*matSize);
    for(int i=0; i<matSize; i++){
        (*returnColumnSizes)[i] = matColSize[i];
    }
    return mat;
}

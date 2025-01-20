// LeetCode 2661. First Completely Painted Row or Column
// 照著 arr[k] 順序將mat對應格子著色，當k是多少時, 剛好將某條 row 或 col 全部著色
int firstCompleteIndex(int* arr, int arrSize, int** mat, int matSize, int* matColSize) {
    int M = matSize, N = matColSize[0];
    int I[M*N+1], J[M*N+1]; // 用陣列「記錄對應的座標」
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            I[mat[i][j]] = i; // 先做 i,j 對照表
            J[mat[i][j]] = j;
        }
    }
    int rows[M], cols[N]; // 可快速確認「是否集滿整條」
    for(int i=0; i<M; i++) rows[i] = 0;
    for(int j=0; j<N; j++) cols[j] = 0;
    for(int k=0; k<arrSize; k++) {
        rows[I[arr[k]]]++;
        cols[J[arr[k]]]++;
        if(rows[I[arr[k]]]==N || cols[J[arr[k]]]==M) return k;
    }
    return -1;
}

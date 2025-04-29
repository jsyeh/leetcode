// LeetCode 311. Sparse Matrix Multiplication
// 進行 sparse 矩陣乘法，裡面有很多項是 0 哦
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** multiply(int** mat1, int mat1Size, int* mat1ColSize, int** mat2, int mat2Size, int* mat2ColSize, int* returnSize, int** returnColumnSizes){
    int M = mat1Size, K = mat2Size, N = mat2ColSize[0];
    int ** ans = (int**)malloc(sizeof(int*)*M);
    for(int i=0; i<M; i++){
        ans[i] = (int*) calloc(N, sizeof(int)); // 都會設為0
    }
    *returnColumnSizes = (int*) malloc(sizeof(int)*M);
    for(int i=0; i<M; i++){
        for(int k=0; k<K; k++){
            if(mat1[i][k]==0) continue; // 避開有0的項，因為0乘任何數都是0
            for(int j=0; j<N; j++){
                ans[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }

    *returnSize = M;
    for(int i=0; i<M; i++){
        (*returnColumnSizes)[i] = N;
//printf("%d ", N);  
    }
    return ans;
}

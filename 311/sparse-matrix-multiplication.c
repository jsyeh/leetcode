/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** multiply(int** mat1, int mat1Size, int* mat1ColSize, int** mat2, int mat2Size, int* mat2ColSize, int* returnSize, int** returnColumnSizes){
    int M = mat1Size, K = mat2Size, N = mat2ColSize[0];
    int ** ans = (int**)malloc(sizeof(int*)*M);
    for(int i=0; i<M; i++) ans[i] = (int*) malloc(sizeof(int)*N);
    *returnColumnSizes = (int*) malloc(sizeof(int)*M);

    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            ans[i][j] = 0;
            for(int k=0; k<K; k++){
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
}//case 9/13: [[0,1],[0,0],[0,1]] [[1,0],[1,0]]

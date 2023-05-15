/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes){
    int r0 = matSize, c0 = matColSize[0];
    if(r*c != r0*c0){
        *returnSize = matSize;
        (*returnColumnSizes) = matColSize;
        return mat; //因為長寬不合,直接結束
    }

    int** ans = (int**) malloc(sizeof(int*)*r);
    *returnSize = r;
    *returnColumnSizes = (int*)malloc(sizeof(int)*r);
    for(int i=0; i<r; i++){
        ans[i] = (int*)malloc(sizeof(int)*c);
        (*returnColumnSizes)[i] = c;
    }
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            int id = i*c+j;
            int i0 = id/c0, j0 = id%c0;
            ans[i][j] = mat[i0][j0];
        }
    }

    return ans;
}

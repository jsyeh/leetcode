// 把2D matrix 以 1D array 來處理，先計算 prefix 及 suffix
// 再把 prefix[i-1] 和 suffix[i+1] 乘起來，即可
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** constructProductMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int M = gridSize, N = gridColSize[0];
    int prefix[M*N], suffix[M*N]; // 放全部的 prefix product 及 suffix product 乘積
    int p = 1, s = 1; //用來累積 prefix product 及 suffix product 乘積
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            prefix[i*N+j] = p = p * (grid[i][j] % 12345) % 12345;
        }
    }
    for(int i=M-1; i>=0; i--){
        for(int j=N-1; j>=0; j--){
            suffix[i*N+j] = s = s * (grid[i][j] % 12345) % 12345;
        }
    }
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            grid[i][j] = 1;
            if(i>0 || j>0) grid[i][j] *= prefix[i*N+j-1]; //左項
            if(i<M-1 || j<N-1) grid[i][j] *= suffix[i*N+j+1]; //右項
            grid[i][j] %= 12345; //收尾要再MOD一次
        }
    }
    *returnSize = M;
    *returnColumnSizes = gridColSize; //回收再利用，就不用自己準備記憶體
    return grid; //回收再利用，就不用自己準備記憶體
}
//case 213/1566: grid = [[3,2,5],[6,4,3],[6,3,1]]  要記得再 %12345
//case 1108/1566: grid = [[68916659],[263909215]] 超大的數, 導致 overflow
// 所以要多做 %12345

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** onesMinusZeros(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    //每次在 C 要準備好 return 所需的 memory 都很麻煩
    int** ans = (int**)malloc(sizeof(int*)*gridSize); //左邊
    *returnSize = gridSize; //這行也要小心
    *returnColumnSizes = (int*)malloc(sizeof(int)*gridSize); //這行易漏
    for(int i=0; i<gridSize; i++){
        ans[i] = (int*)malloc(sizeof(int)*gridColSize[i]); //補右邊全部
        (*returnColumnSizes)[i] = gridColSize[i]; //這行易寫錯
    }
    int M = gridSize, N = gridColSize[0]; //換成我熟悉的 M, N
    int onesRow[M], zerosRow[M], onesCol[N], zerosCol[N]; //GNU C++ 擴充語法
    for(int i=0; i<M; i++){ //記得將陣列清為0
        onesRow[i] = 0;
        zerosRow[i] = 0;
    }
    for(int j=0; j<N; j++){ //記得將陣列清為0
        onesCol[j] = 0;
        zerosCol[j] = 0;
    }
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]==1){ //逐個統計 ones 及 zero
                onesRow[i]++;
                onesCol[j]++;
            }else{
                zerosRow[i]++;
                zerosCol[j]++;
            }
        }
    }
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){ //照公式，把答案算出來
            ans[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j];
        }
    }
    return ans;
}

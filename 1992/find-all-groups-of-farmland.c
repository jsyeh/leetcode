// 要找到長方形，回傳它們的「左上、右下」座標
// 不過 C 語言「準備memory」有夠複雜的。
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** ans = NULL; //多筆測資，可重覆利用
int* ansCol = NULL;
int** findFarmland(int** land, int landSize, int* landColSize, int* returnSize, int** returnColumnSizes) {
    if(ans==NULL) { // 準備 memory 有一堆指標，很容易出錯
        ans = (int**)malloc(sizeof(int**)*90000);
        int*temp = (int*)malloc(sizeof(int)*90000*4); // 最多9萬格
        for(int i=0; i<90000; i++) ans[i] = &(temp[i*4]);
        ansCol = (int*)malloc(sizeof(int*)*90000);
        for(int i=0; i<90000; i++) ansCol[i] = 4; //都4個
    }
    int ansN = 0;
    for(int i=0; i<landSize; i++) {
        for(int j=0; j<landColSize[i]; j++) {
            if(land[i][j]==1) { // 找到一個長方塊的開始
                ans[ansN][0]=i;
                ans[ansN][1]=j;
                for(int i2=i; i2<landSize; i2++) { // 查看「高度」
                    if(land[i2][j]==1) ans[ansN][2] = i2;
                    else break; // 遇到盡頭跳開
                }
                for(int j2=j; j2<landColSize[i]; j2++) { // 查看「寬度」
                    if(land[i][j2]==1) ans[ansN][3] = j2;
                    else break; // 遇到盡頭跳開
                }
                for(int i2=i; i2<=ans[ansN][2]; i2++) {
                    for(int j2=j; j2<=ans[ansN][3]; j2++) {
                        land[i2][j2] = 0; //清為0
                    }
                }
                ansN++; //確認多1筆資料
            }
        }
    }
    *returnColumnSizes = ansCol;
    *returnSize = ansN;
    return ans;
}

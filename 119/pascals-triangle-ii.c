/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize){
    int N = rowIndex;
    int* ans = (int*)malloc(sizeof(int)*(N+1));
    for(int i=0; i<=rowIndex; i++){
        ans[0] = 1; //最左邊的1
        ans[i] = 1; //最右邊的1, 而最
        for(int k=i-1; k>0; k--){ //補齊中間的，從右到左，就不會疊到新值
            ans[k] = ans[k] + ans[k-1]; 
        }
    }

    *returnSize = N+1;
    return ans;
}

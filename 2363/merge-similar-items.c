/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
struct two {
    int a[2];
    //int value;
    //int weight;
};
int cmp(const void*p1, const void*p2) {
    const int *a = *(const int **)p1;
    const int *b = *(const int **)p2;
    return a[0] - b[0];
}
int** mergeSimilarItems(int** items1, int items1Size, int* items1ColSize, int** items2, int items2Size, int* items2ColSize, int* returnSize, int** returnColumnSizes) {
    int** ans = (int**)malloc(sizeof(int*)*(items1Size+items2Size));
    qsort(items1, items1Size, sizeof(struct two), cmp);
    qsort(items2, items2Size, sizeof(struct two), cmp);
    int N = 0;
    for(int i=0, j=0; i<items1Size || j<items2Size; ) {
        if(i<items1Size && j<items2Size) {
            if(items1[i][0]==items2[j][0]) {
                ans[N] = (int*)malloc(sizeof(int)*2);
                ans[N][0] = items1[i][0];
                ans[N++][1] = items1[i][1] + items2[j][1];
                i++;
                j++;
            } else if(items1[i][0]<items2[j][0]) {
                ans[N] = (int*)malloc(sizeof(int)*2);
                ans[N][0] = items1[i][0];
                ans[N++][1] = items1[i][1];
                i++;
            } else {
                ans[N] = (int*)malloc(sizeof(int)*2);
                ans[N][0] = items2[j][0];
                ans[N++][1] = items2[j][1];
                j++;
            }
        } else if(i<items1Size){
            ans[N] = (int*)malloc(sizeof(int)*2);
            ans[N][0] = items1[i][0];
            ans[N++][1] = items1[i][1];
            i++;
        } else {
            ans[N] = (int*)malloc(sizeof(int)*2);
            ans[N][0] = items2[j][0];
            ans[N++][1] = items2[j][1];
            j++;
        }
    }
    int* ansN = (int*)malloc(sizeof(int)*N);
    for(int i=0; i<N; i++) ansN[i] = 2;
    *returnColumnSizes = ansN;
    *returnSize = N;
    return ans;
}

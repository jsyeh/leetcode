/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int comp(const void *p1, const void *p2){
    int* row1 = (int*)p1;
    int* row2 = (int*)p2;
    if(row1[0]!=row2[0]) return row1[0]-row2[0];
    return row1[1]-row2[1];
}
int* kWeakestRows(int** mat, int matSize, int* matColSize, int k, int* returnSize){
    int M = matSize, N = matColSize[0];
    int soldier[M][2];//soldier[i][1]=i;
    for(int i=0; i<M; i++){
        soldier[i][0] = 0; //這個是存有幾個軍人
        for(int j=0; j<N; j++){
            if(mat[i][j]==1){
                soldier[i][0]++;
            }else break;
        }
        soldier[i][1] = i;//這個存對應原始的i row
    }
    qsort(soldier, M, sizeof(int)*2, comp);
    int* ans = (int*)malloc(sizeof(int)*k);
    *returnSize = k;
    for(int i=0; i<k; i++){
        ans[i] = soldier[i][1];
    }
    return ans;
}

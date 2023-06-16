/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSmallestSetOfVertices(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize){
    int in[n];
    for(int i=0; i<n; i++) in[i] = 0;

    for(int i=0; i<edgesSize; i++) {
        int from = edges[i][0];
        int to = edges[i][1];
        in[to]++;
    }

    int ansN=0;
    for(int i=0; i<n; i++){
        if(in[i]==0) ansN++;
    }

    int * ans = (int*) malloc(sizeof(int)*ansN);
    ansN = 0;
    for(int i=0; i<n; i++){
        if(in[i]==0) ans[ansN++] = i;
    }
    *returnSize = ansN;
    return ans;
}

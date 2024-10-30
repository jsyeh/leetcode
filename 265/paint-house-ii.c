// LeetCode 265. Paint House II
// 用k種色彩的油漆，漆 n 間房子，相鄰不同色
int minCostII(int** costs, int costsSize, int* costsColSize) {
    int N = costsSize, K = costsColSize[0];
    // cost[i][k] 漆房子i用色彩k的費用
    int table[N+1][K]; // table[i][k] 考慮前i間的第i間漆k色的(最便宜)答案
    for(int k=0; k<K; k++) table[0][k] = 0; // 0間房，0元

    for(int i=1; i<=N; i++) {
        for(int k=0; k<K; k++) {
            int min = INT_MAX;
            for(int kk=0; kk<K; kk++) {
                if(k!=kk && table[i-1][kk]<min) min = table[i-1][kk];
            }
            table[i][k] = min + costs[i-1][k];
        }
    }
    int ans = INT_MAX;
    for(int k=0; k<K; k++) {
        if(table[N][k]<ans) ans = table[N][k];
    }
    return ans;
}

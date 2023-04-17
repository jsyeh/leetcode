int minCostClimbingStairs(int* cost, int costSize){
    int table[1001];
    table[0] = 0;//cost[0];
    table[1] = 0;//cost[1];
    for(int i=2; i<=costSize; i++){
        table[i] = min(table[i-1]+cost[i-1], table[i-2]+cost[i-2]);
        printf("%d\n", table[i]);
    }
    return table[costSize];
}
int min(int a, int b) {
    if(a<b) return a;
    else return b;
}

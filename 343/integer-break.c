int max(int a, int b){
    if(a>b) return a;
    else return b;
}

int integerBreak(int n){
    int table[n+1];
    table[0] = 1;
    table[1] = 1;
    table[2] = 1;
    for(int i=3; i<=n; i++){
        int tempMax = table[i-1]; //暫時的最大值
        for(int k = 1; k<i; k++){
            int part1 = max(i-k, table[i-k]); //1個，或拆2個以上
            int part2 = max(k, table[k]); //1個，或拆2個以上
            if(part1*part2>tempMax) tempMax = part1*part2;
        }
        table[i] = tempMax;
    }
    return table[n];
}

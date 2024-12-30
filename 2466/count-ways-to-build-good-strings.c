int countGoodStrings(int low, int high, int zero, int one){
    long long table[high+1];
    //table[i]表示剛好有i個字母 的排列組合總數
    //所以答案是 table[low] 加到 table[high]
    table[0] = 1;
    for(int i=1; i<=high; i++){
        table[i] = 0;
        if(i-one>=0) table[i] += table[i-one];
        if(i-zero>=0) table[i] += table[i-zero];
        table[i] = table[i] % 1000000007;
        //printf("%lld\n", table[i]);
    }
    long long ans = 0;
    for(int i=low; i<=high;i++){
        ans = (ans + table[i]) % 1000000007;
    }
    return (int)ans;
}

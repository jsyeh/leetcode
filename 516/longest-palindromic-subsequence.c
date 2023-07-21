int longestPalindromeSubseq(char * s){
    //這個題目，可以簡化成：找到兩字串的 longest common subsequence
    int N = strlen(s);
    char t[N+1];
    for(int i=0; i<N; i++){
        t[N-1-i] = s[i];
    }
    t[N] = 0;
    int table[N+1][N+1]; //table[i][j] 表示 prefix i vs. prefix j 的最長common
    for(int i=0; i<N; i++){
        table[i][0] = 0;
        table[0][i] = 0; 
    }
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(s[i-1]==t[j-1]){ //真幸運，有相同
                table[i][j] = table[i-1][j-1] + 1;
            }else{
                table[i][j] = table[i-1][j];
                if(table[i][j-1]>table[i][j]) table[i][j] = table[i][j-1];
            }
        }
    }
    return table[N][N];
}

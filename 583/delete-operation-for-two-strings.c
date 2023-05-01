int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int minDistance(char * word1, char * word2){
    //反過來的問題，其實是 Longest Common Sequence的反過來的問題
    int N1 = strlen(word1);
    int N2 = strlen(word2);
    int table[N1+1][N2+1];//供LCS使用,table[i][j]的LCS長度

    for(int i=0; i<=N1; i++) table[i][0] = 0;
    for(int j=0; j<=N2; j++) table[0][j] = 0;

    for(int i=1; i<=N1; i++){
        for(int j=1; j<=N2; j++){
            if(word1[i-1]==word2[j-1]) table[i][j] = table[i-1][j-1]+1;
            else table[i][j] = max(table[i][j-1], table[i-1][j]);
        }
    }
    return N1+N2-table[N1][N2]-table[N1][N2];
}

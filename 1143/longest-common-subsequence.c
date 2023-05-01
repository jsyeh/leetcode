int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int longestCommonSubsequence(char * text1, char * text2){
    int N1 = strlen(text1);
    int N2 = strlen(text2);
    int table[N1+1][N2+1];//table[0][0]表示都取0個字母 的長度
    for(int i=0; i<=N1; i++) table[i][0] = 0;
    for(int j=0; j<=N2; j++) table[0][j] = 0;

    for(int i=1; i<=N1; i++){ //text1 使用前i個字母
        for(int j=1; j<=N2; j++){ //text2 使用前j個字母
            if(text1[i-1]==text2[j-1]){
                table[i][j] = table[i-1][j-1]+1; //多1個字母符合
            }else table[i][j] = max(table[i-1][j], table[i][j-1]);
        }
    }
    return table[N1][N2];
}

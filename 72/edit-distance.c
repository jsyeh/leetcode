int minDistance(char * word1, char * word2){
    int N1 = strlen(word1);
    int N2 = strlen(word2);

    int table[N1+1][N2+1]; //table[i][j] 表示使用 i個字母 j個字母的子問題，答案
    for(int i=0; i<=N1; i++) table[i][0] = i; 
    for(int j=0; j<=N2; j++) table[0][j] = j; //需要刪一堆字母

    for(int i=1; i<=N1; i++){
        for(int j=1; j<=N2; j++){
            if(word1[i-1]==word2[j-1]){ //有相同的字，太好了
                table[i][j] = table[i-1][j-1];
            }else{
                table[i][j] = INT_MAX;
            }
            int e1 = table[i-1][j] + 1;
            int e2 = table[i][j-1] + 1;
            int e3 = table[i-1][j-1] + 1;
            int e12 = (e1<e2) ? e1 : e2;
            int e123 = (e3<e12)? e3 : e12;
            if(e123 < table[i][j]) table[i][j] = e123;
        }
    }
    return table[N1][N2];
}

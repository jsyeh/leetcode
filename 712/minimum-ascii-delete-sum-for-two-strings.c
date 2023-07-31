int minimumDeleteSum(char * s1, char * s2){
    int N1 = strlen(s1), N2 = strlen(s2);
    int table[N1+1][N2+1]; //table[i][j] 長度為 i, j 的兩字串的 minDelSum

    //照著題目，把要刪掉的字母的ASCII值，加到 table[i][0] 及 table[0][j]裡
    table[0][0] = 0;
    for(int i=1; i<=N1; i++) table[i][0] = table[i-1][0] + s1[i-1];
    for(int j=1; j<=N2; j++) table[0][j] = table[0][j-1] + s2[j-1];

    for(int i=1; i<=N1; i++){
        for(int j=1; j<=N2; j++){
            //對應字母相同，table[i][j] 照舊
            if(s1[i-1]==s2[j-1]) table[i][j] = table[i-1][j-1];
            else{
                //對應字母不同，看兩種不同的刪法，對應的值哪個小，用它
                int d1 = table[i-1][j] + s1[i-1]; //i那個字串
                int d2 = table[i][j-1] + s2[j-1]; //j那個字串
                table[i][j] = (d1<d2)?d1:d2;
            }
        }
    }
    return table[N1][N2];
}

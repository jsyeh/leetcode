int N; //字串長度
int helper(char *s, int i, int* table){
    if(table[i]!=0) return table[i]; //之前有記憶的答案
    if(i==N) return 1; //順利解到最後，算是1種可能
    if(s[i]=='0') return 0; //不合理 leading zero
    if(i==N-1) return 1; //最後的字母

    if(s[i]=='1' || (s[i]=='2' && i+1<N && s[i+1]<='6')){
        table[i+1] = helper(s, i+1, table);
        table[i+2] = helper(s, i+2, table);
        return table[i+1] + table[i+2];
    }else{
        table[i+1] = helper(s, i+1, table);
        return table[i+1];
    }
}
int numDecodings(char * s){
    N = strlen(s);
//printf("N:%d\n", N);
    int table[102]={};
    return helper(s, 0, table);
}
//case 55/269: "0"
//另一種不可能 "340"

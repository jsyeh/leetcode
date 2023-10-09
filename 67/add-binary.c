int max(int n1, int n2){
    if(n1>n2) return n1;
    else return n2;
}
char * addBinary(char * a, char * b){
    int N1 = strlen(a), N2 = strlen(b), N = max(N1,N2);
    int carry = 0;
    char * ans = (char*) malloc(sizeof(char)*(N+2)); //有多要1+1格
    ans[N+1] = 0; //字串結尾佔最後1格
    for(int i=0; i<N; i++){
        if(i<N1) carry += a[N1-1-i] - '0';
        if(i<N2) carry += b[N2-1-i] - '0';
        ans[N-i] = carry%2 + '0';
        carry /= 2;
    }
    if(carry>0){
        ans[0] = '1'; //最前面進位的話，也佔掉1格
        return ans; //用掉預留的那個，不用右移一格，直接回傳
    }else{
        return ans+1; //沒用到込趇，少用一格（事先有多要一格memory）
    }
}

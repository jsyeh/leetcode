// 「最差」也只要刪「2步」：先刪全部的'a'(一定是迴圈)，再刪剩下的'b'
// 所以如果「已經是迴圈」就return 1 不然就 return 2

int removePalindromeSub(char* s) {
    int N = strlen(s); //先了解字串長度
    for(int i=0; i<N/2; i++) {
        if(s[i] != s[N-1-i]) return 2; //不是迴圈，要2步
    }
    return 1; //是迴文，只要1步
}

// LeetCode 7. Reverse Integer
// 將 123 變 321
int reverse(int x){
    int sign = 1;
    long long int n = x, ans = 0;
    if(n<0) {
        sign = -1; // 先取出「正負號」
        n = -n; // 將 n 變成「正數」
    }
    while(n>0) { // 利用「剝皮法」逐位取出來
        ans = ans * 10 + n % 10; // 再逐位組回去
        n = n / 10;
    }
    ans = ans * sign; // 把「正負號」放扣去
    if(ans<INT_MIN || ans>INT_MAX) return 0; // 題目強調「數字超過範圍」要 return 0
    return ans;
}

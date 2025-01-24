// LeetCode 1071. Greatest Common Divisor of Strings
// 只要 str1+str2 != str2+str1 就代表不正確。接下來查長度的 gcd() 可快速找到答案
int gcd(int a, int b) {
    if(a==0) return b;
    if(b==0) return a;
    return gcd(b, a%b);
}
char* gcdOfStrings(char* str1, char* str2) {
    int N1=strlen(str1), N2=strlen(str2);
    char str1str2[N1+N2+1], str2str1[N1+N2+1];
    strcpy(str1str2, str1); // 先把字串 str1 放左邊
    strcat(str1str2, str2); // 再把字串 str2 放右邊，就完成 str1str2
    strcpy(str2str1, str2); // 先把字串 str2 放左邊
    strcat(str2str1, str1); // 再把字串 str1 放右邊，就完成 str2str1
    if(strcmp(str1str2, str2str1) != 0) return "";

    int ans = gcd(N1, N2);
    str1[ans]=0;
    return str1;    
}

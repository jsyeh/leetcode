// 之前曾用 Python 寫過, 只要 str1+str2 != str2+str1 就代表不正確。接下來查長度的 gcd()
int gcd(int a, int b) {
    if(a==0) return b;
    if(b==0) return a;
    return gcd(b, a%b);
}
char* gcdOfStrings(char* str1, char* str2) {
    int N1=strlen(str1), N2=strlen(str2);
    char all1[N1+N2+1], all2[N1+N2+1];
    for(int i=0; i<N1; i++) all1[i] = str1[i];
    for(int i=0; i<N2; i++) all1[N1+i] = str2[i];
    for(int i=0; i<N2; i++) all2[i] = str2[i];
    for(int i=0; i<N1; i++) all2[N2+i] = str1[i];
    all1[N1+N2]=0;
    all2[N1+N2]=0;
    if(strcmp(all1,all2)!=0) return "";

    int ans = gcd(N1,N2);
    str1[ans]=0;
    return str1;    
}

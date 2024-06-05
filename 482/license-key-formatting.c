char* licenseKeyFormatting(char* s, int k) {
    int j = 0;  // 左邊的 s[j] 的 index
    for(int i=0; s[i]!=0; i++) { // 將 s[j] = s[i] 往前移
        if(s[i]>='0' && s[i]<='9') s[j++] = s[i];  // 照搬數字
        else if(s[i]>='A' && s[i]<='Z') s[j++] = s[i];  // 照搬大寫字母
        else if(s[i]>='a' && s[i]<='z') s[j++] = s[i]  + 'A' - 'a'; // 轉大寫
    }
    int N = j; //有效英數字的總數
    char* ans = (char*) malloc(sizeof(char)*(N+N/k+1)); // 準備足夠大的字串空間
    j = 0;  // 左邊 ans[j] 的 index
    for(int i=0; i<N; i++){
        ans[j++] = s[i];  // 逐格搬移
        if(i%k==(N-1)%k && i!=N-1) ans[j++] = '-';  // 補上 '-'
    }
    ans[j] = '\0';  // 補字串結尾
    return ans;
}

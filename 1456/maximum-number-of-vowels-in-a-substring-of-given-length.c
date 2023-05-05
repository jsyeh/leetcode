int maxVowels(char * s, int k){  //指標就是陣列、陣列就是指標  s[i]
    int N = strlen(s); //字串長度
    int a[N];//這寫法,只能在(CodeBlocks)GNU C/C++使用,不能在 Microsoft VC使用
    int vo=0, ans=0, len=0;
    for(int i=0; i<N; i++){
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u'){
            vo++;//多一個母音
        }
        a[i] = vo;//到目前為止的母音
printf("%d ", a[i]);
        if(i>=k) len = a[i] - a[i-k];
        else len = a[i];
        if(len>ans) ans = len;
    }
    
    return ans;
}//case 18/106: "weallloveyou" 7

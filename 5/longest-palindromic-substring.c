char * longestPalindrome(char * s){
    int N = strlen(s);
    int ans=0, start=0, end=0;
    for(int i=0; i<N; i++){
        //如果是奇數的Palindrome,那中心點在i
        int len=1;
        for(int m=1; i-m>=0 && i+m<N; m++){
            if(s[i-m] == s[i+m]) len+=2;
            else break;
        }
        if(len>ans){
            ans = len;
            start = i-len/2;
            end = start+ans;
            //printf("i:%d len:%d start:%d end:%d\n", i, len, start, end);
        }

        //如果是偶數的Palindrome,那中心點在 i,i+1間
        len=0;
        for(int m=0; i-m>=0 && i+1+m<N; m++){
            if(s[i-m] == s[i+1+m]) len+=2;
            else break;
        }
        if(len>ans){
            ans = len;
            start = i-len/2+1;
            end = start+ans;
        }
    }
    //printf("ans:%d\n", ans);
    s[end]=0;
    return s+start;
}//case 77/141: "aacabdkacaa"
//case 84/141: "abbcccbbbcaaccbababcbcabca"

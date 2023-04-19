int longestPalindrome(char * s){
    int ans=0;
    int H1[26]={};
    int H2[26]={};
    while(*s!=0){
        if(*s>='a'&& *s<='z') H1[*s-'a']++;
        else H2[*s-'A']++;
        s++;
    }
    int odd=0;
    for(int i=0; i<26; i++){
        if(H1[i]%2==1) odd=1;
        if(H2[i]%2==1) odd=1;
        ans += H1[i]/2*2;
        ans += H2[i]/2*2;
    }
    if(odd==1) ans++;
    return ans;
}//case 26/95: "AAAAAA"

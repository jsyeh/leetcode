int numberOfSpecialChars(char* word) {
    int H1[26]={}, H2[26]={};
    for(int i=0; word[i]!=0; i++){
        char c = word[i];
        if(c>='A' && c<='Z') H1[c-'A']++;
        else if(c>='a' && c<='z') H2[c-'a']++;
    }
    int ans = 0;
    for(int i=0; i<26; i++){
        if(H1[i]>0 && H2[i]>0) ans++;
    }
    return ans;
}

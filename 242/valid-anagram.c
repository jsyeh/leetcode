bool isAnagram(char * s, char * t){
    int H1[26]={}, H2[26]={};
    int N1 = strlen(s), N2 = strlen(t);
    if(N1!=N2) return false;

    for(int i=0; i<N1; i++){
        H1[s[i]-'a']++;
        H2[t[i]-'a']++;
    }
    for(int i=0; i<26; i++){
        if(H1[i]!=H2[i]) return false;
    }
    return true;
}

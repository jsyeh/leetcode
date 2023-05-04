char * frequencySort(char * s){
    int N = strlen(s);
    int H[62]={};
    for(int i=0; s[i]!=0; i++){
        if(s[i]>='A'&&s[i]<='Z') H[s[i]-'A']++;
        if(s[i]>='a'&&s[i]<='z') H[s[i]-'a'+26]++;
        if(s[i]>='0'&&s[i]<='9') H[s[i]-'0'+52]++;
    }
    char a[62];
    for(int i=0; i<26; i++) a[i] = 'A'+i;
    for(int i=0; i<26; i++) a[i+26] = 'a'+i;
    for(int i=0; i<10; i++) a[i+52] = '0'+i;

    char * ans = (char*) malloc(sizeof(char)*N+1);
    ans[N]=0;

    for(int i=0; i<62; i++){
        for(int j=i+1; j<62; j++){
            if(H[i]<H[j]){
                int temp = H[i];
                H[i] = H[j];
                H[j] = temp;
                char c = a[i];
                a[i] = a[j];
                a[j] = c;
            }
        }
    }
    int len=0;
    for(int i=0; i<62; i++){
        for(int k=0; k<H[i]; k++){
            ans[len++]=a[i];
        }
    }

    return ans;
}

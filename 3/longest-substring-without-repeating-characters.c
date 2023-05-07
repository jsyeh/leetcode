int lengthOfLongestSubstring(char * s){
    int N = strlen(s);
    if(N==0) return 0;

    int H[256]={};

    int ans = 1;
    int i=0, j=1; //i:left, j:right
    H[s[0]]++;
    while(j<N){
        H[s[j]]++;
        if(H[s[j]]>1){ //有重覆出現了
            while(H[s[j]]>1){
                H[s[i]]--; //左邊一直縮，直到沒有重覆為止
                i++;
            }
            j++;
        }else{
            j++;
            if(j-i>ans) ans = j-i;
        }
    }
    return ans;
}

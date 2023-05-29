/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void compareAndAdd(int* H1, int* H2, int* ans, int k, int* returnSize){
    for(int i=0; i<26; i++){
        if(H1[i]!=H2[i]) return;
    }
    ans[*returnSize] = k;
    (*returnSize)++; //要小心，這裡我忘了圓括號，就錯了
}
int* findAnagrams(char * s, char * p, int* returnSize){
    int H1[26] = {};
    int H2[26] = {};
    int N1 = strlen(s), N2 = strlen(p);
    int* ans = (int*)malloc(sizeof(int)*N1);
    *returnSize = 0;
    if(N2>N1){
        return ans;
    }

    for(int i=0; i<N2; i++){
        H2[p[i]-'a']++;
        H1[s[i]-'a']++;
    }
    compareAndAdd(H1,H2, ans, 0, returnSize);

    for(int i=0; i<N1-N2; i++){
        H1[s[i+N2]-'a']++;
        H1[s[i]-'a']--;
        compareAndAdd(H1, H2, ans, i+1, returnSize);
    }
    return ans;
}

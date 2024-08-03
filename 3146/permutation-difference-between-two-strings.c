int findPermutationDifference(char* s, char* t) {
    int pos[26] = {};
    for(int i=0; s[i]!=0; i++){
        pos[s[i]-'a'] = i;
    }
    int ans = 0;
    for(int i=0; t[i]!=0; i++){
        ans += abs(i-pos[t[i]-'a']);
    }
    return ans;
}

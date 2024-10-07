// LeetCode 1967. Number of Strings That Appear as Substrings in Word
// 問 pattern 裡，有幾個是 word 的子字串
int numOfStrings(char** patterns, int patternsSize, char* word) {
    int ans = 0;
    for(int i=0; i<patternsSize; i++){
        if(strstr(word, patterns[i]) != NULL) ans++;
    }
    return ans;
}

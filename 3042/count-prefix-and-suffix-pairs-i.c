// LeetCode 3042. Count Prefix and Suffix Pairs I
// 左邊 words[i] 是不是 右邊 words[j] 的prefix兼postfix (剛好是字首、也是字尾)
int countPrefixSuffixPairs(char** words, int wordsSize) {
    int ans = 0;
    int L[wordsSize]; // 想先將全部字的長度,都先算出來
    for(int i=0; i<wordsSize; i++) L[i] = strlen(words[i]);

    for(int i=0; i<wordsSize; i++) { // 左邊 words[i]
        for(int j=i+1; j<wordsSize; j++) { // 右邊 words[j]
            if(L[i]>L[j]) continue;
            int d = L[j] - L[i]; // 字串長度差, 比較「字尾」
            int bad = 0;
            for(int k=0; k<L[i]; k++) { // 逐個字母處理
                if(words[i][k] != words[j][k] || words[i][k] != words[j][d+k]) {
                    bad = 1;
                    break;
                }
            }
            if(bad==0) ans++;
        }
    }
    return ans;
}

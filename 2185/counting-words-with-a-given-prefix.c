// LeetCode 2185. Counting Words With a Given Prefix
// 給字串 pref，在 words 裡，找有幾個字串的字首與 pref 相同
int prefixCount(char** words, int wordsSize, char* pref) {
    int ans = 0;
    for(int i=0; i<wordsSize; i++) { // 每個字都去測
        int possible = 1; // 一開始還有可能哦
        for(int k=0; pref[k]!=0; k++) {
            if(words[i][k] != pref[k]) { // 不相同
                possible = 0; // 不可能是答案
                break;
            } // 如果都沒有被 break 掉，就是還可能、正確。
        }
        ans += possible; // 可能就會 +1 不可能就會 +0
    }
    return ans;
}

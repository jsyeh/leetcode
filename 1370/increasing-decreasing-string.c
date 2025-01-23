// LeetCode 1370. Increasing Decreasing String
// s 要變出新字串，規則：先挑最小，再挑「不重覆」的最小，直到挑不到。
// 再挑大，再挑「不重覆」的最大，直到挑不到。重覆做。
char* sortString(char* s) {
    int freq[26] = {}; // 存放 26 個字母的出現次數
    for(int i=0; s[i]!=0; i++) {
        freq[s[i]-'a']++;
    }
    int counter[26][2], counterN = 0;
    for(int i=0; i<26; i++) { // 建立精簡的 counter 表格數量
        if(freq[i]!=0) {
            counter[counterN][0] = i;
            counter[counterN++][1] = freq[i];
        }
    }
    int si = 0;
    while(counterN>0) { // 持續做到 counter 用完
        for(int i=0; i<counterN; i++) {
            s[si++] = counter[i][0] + 'a';
            counter[i][1]--;
            if(counter[i][1]==0) { // 某個字母用盡
                for(int k=i; k<counterN-1; k++) {
                    counter[k][0] = counter[k+1][0];
                    counter[k][1] = counter[k+1][1];
                }
                counterN--; // 能用的字母減少了
                i--; // 補回，以便下一輪能正確拼接
            }
        }
        for(int i=counterN-1; i>=0; i--) { // 大到小
            s[si++] = counter[i][0] + 'a';
            counter[i][1]--;
            if(counter[i][1]==0) { // 某個字母用盡
                for(int k=i; k<counterN-1; k++) {
                    counter[k][0] = counter[k+1][0];
                    counter[k][1] = counter[k+1][1];
                }
                counterN--; // 能用的字母減少了
            }
        }
    }
    return s; // 重覆使用字串 s 當答案
}

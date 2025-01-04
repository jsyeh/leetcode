// LeetCode 1930. Unique Length-3 Palindromic Subsequences
// 在字串 s 可跳著挑 3個字母，有幾種可能的 palindrome 迴文。
// 3個字母只要「頭尾相同」，即是「迴文」。先記錄字串中「每種字母」頭尾位置即可。
int countPalindromicSubsequence(char* s) {
    int first[26] = {}, last[26] = {}; // 26個字母，預設值都先放0
    for(int i=0; s[i]!=0 ; i++) {
        int c = s[i] - 'a'; // 字母 s[i] 是 26 字母的第幾個
        if(first[c]==0) first[c] = i+1; // 第1次出現的話，預設值是0。所以我稍移1格，避開0
        last[c] = i+1; // 稍移1格
    }
    int ans = 0; // 統計「有幾種」字
    for(int c=0; c<26; c++) { // 針對 26 個字母，當字首、字尾
        int middle[26] = {}; // 放在中間的字母
        for(int i=first[c]; i<last[c]-1; i++) { // 之前 first[c] last[c] 有稍移1格
            if(middle[s[i]-'a']==0) ans++;
            middle[s[i]-'a'] = 1;
        }
    }
    return ans;
}


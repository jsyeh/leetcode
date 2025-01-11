// LeetCode 1400. Construct K Palindrome Strings
// 能用字串 s 的字母，調整順序後，切成 k 個 palindrome 迴文嗎？
bool canConstruct(char* s, int k) {
    int N = 0;
    int freq[26] = {}; // 統計字母出現次數
    for(int i=0; s[i]!=0; i++) { // 字串的迴圈
        freq[s[i]-'a']++;
        N++; // 用來計算字串的長度（有機會與i合併，不過怕符號混在一起，所以分開）
    }
    if(N<k) return false; // 字母不夠用，失敗

    for(int i=0; i<26; i++) {
        if(freq[i]%2==1) k--; // 奇數用掉1個迴文的額度
    }
    if(k<0) return false; // 奇數的字母太多，無法分配，失敗
    return true; // 最後成功
}

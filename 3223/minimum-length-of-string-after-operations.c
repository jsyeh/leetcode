// LeetCode 3223. Minimum Length of String After Operations
// 字串 s 挑 s[i]，左邊、右邊都至少有1格與s[i]相同，把「左右最近」的2個刪掉。
// 持續做，s要變最短。其實是「相同字母」3個以上時，每次減2個，一直做。
// 模擬不同的數量，發現結果是 0,1,2 接下來 1 2 1 2 循還。
int minimumLength(char* s) {
    int freq[26] = {}; // 統計26個字母的出現次數
    for(int i=0; s[i] != 0; i++) { // 字串的迴圈
        freq[s[i]-'a']++;
    }
    int ans = 0;
    for(int i=0; i<26; i++) { // 針對 26 個字母
        if(freq[i]==0) continue; // 沒有長度
        ans += (freq[i]-1) % 2 + 1; // 另一個可以用的公式
    } // 剩下的，都是 1 2 1 2 循環，也就是「減1」再 % 2 再「加1」即可
    return ans;
}

// LeetCode 409. Longest Palindrome
int longestPalindrome(char * s){
    int ans = 0, H1[26] = {}, H2[26] = {};  // 統計大小寫字母的出現次數
    for(int i=0; s[i]!=0; i++) {
        if(s[i]>='a' && s[i]<='z') H1[s[i]-'a']++;  // 小寫字母
        else H2[s[i]-'A']++;  // 大寫字母
    }  // 先統計小寫、大寫的字母出現次數
    int odd = 0;  // 查看出現次數「有沒有奇數」
    for(int i=0; i<26; i++){
        if(H1[i]%2==1) odd = 1;
        if(H2[i]%2==1) odd = 1;
        ans += H1[i] / 2 * 2;
        ans += H2[i] / 2 * 2;
    }
    if(odd==1) ans++;
    return ans;
}

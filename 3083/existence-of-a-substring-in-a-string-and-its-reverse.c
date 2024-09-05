// LeetCode 3083. Existence of a Substring in a String and Its Reverse
// 只要有「substring」及「它的反過來的substring」就是 True
bool isSubstringPresent(char* s) {
    int table[26][26] = {}; // table[a][b] 對應 字母a 後面有 字母b
    if(s[1]==0) return false; // 長度為1的字串，不會有2個字母的 substring
    for(int i=1; s[i]!=0; i++) {
        int a = s[i-1]-'a', b = s[i]-'a';
        table[a][b]=1; // ab 出現了
        if(table[b][a]==1) return true; //反過來的ba 也有出現過
    }
    return false;
}

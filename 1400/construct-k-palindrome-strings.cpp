// LeetCode 1400. Construct K Palindrome Strings
// 能用字串 s 的字母，調整順序後，切成 k 個 palindrome 迴文嗎？
class Solution {
public:
    bool canConstruct(string s, int k) {
        if(s.length()<k) return false; // 字串長度不足，會失敗
        
        int freq[26] = {}; // 統計字母出現次數
        for(int i=0; i<s.length(); i++) {
            freq[s[i]-'a']++;
        }
        for(int i=0; i<26; i++) {
            if(freq[i]%2==1) k--; // 每出現一個奇數，就需用掉1個palindrome的額度
        }
        if(k<0) return false; // 額度不夠用，失敗
        return true; // 最後成功
    }
};

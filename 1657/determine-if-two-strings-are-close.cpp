// LeetCode 1657. Determine if Two Strings Are Close
// 它的操作，是任意交換位置，還可以任意字母對調翻轉。所以統計好數量，並看字母set相同，就成功
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if(word1.length() != word2.length()) return false; // 長度要相同
        vector<int> counter1(26,0); // 26個字母，預設值 0
        vector<int> counter2(26,0); // 26個字母，預設值 0
        for(char c : word1) counter1[c-'a']++; // 統計字母出現次數
        for(char c : word2) counter2[c-'a']++; // 統計字母出現次數

        for(int i=0; i<26; i++){ // 字母「一邊有、一邊沒有」，就失敗
            if(counter1[i]!=0 && counter2[i]==0) return false;
            if(counter1[i]==0 && counter2[i]!=0) return false;
        }
        sort(counter1.begin(), counter1.end()); // 照頻率排序
        sort(counter2.begin(), counter2.end()); // 照頻率排序
        for(int i=0; i<26; i++) { // 若數量不同，就失敗
            if(counter1[i] != counter2[i]) return false;
        }
        return true;
    }
};

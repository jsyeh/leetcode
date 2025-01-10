// LeetCode 916. Word Subsets
// 從 words1 挑出合格的字：這些字裡，有 words2的「每個字」的「全部字母」
class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        int words2set[26] = {}; // 用來放 words2 裡「每個字」的字母上限
        for(string word : words2) {
            int now[26] = {}; // 現在這個字的統計數量
            for(char c : word) {
                now[c-'a']++; // 累積現在這個字的字母數量
            }
            for(int i=0; i<26; i++) { // 更新「字母上限」
                words2set[i] = max(words2set[i], now[i]);
            }
        }
        vector<string> ans; // 現在開始找答案
        for(string word : words1) { // 逐一檢測 words1 的字
            int now[26] = {}; // 現在這個字的統計數量
            for(char c : word) {
                now[c-'a']++; // 累積現在這個字的字母數量
            }
            int bad = 0;
            for(int i=0; i<26; i++) { // 更新「字母上限」
                if(now[i] < words2set[i]) { // 如果「字母不足」
                    bad = 1; // 就失敗
                    break;
                }
            }
            if(bad==0) ans.push_back(word);
        }
        return ans;
    }
};

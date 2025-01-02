// LeetCode 2559. Count Vowel Strings in Ranges
// words[i] 裡由母音（a e i o u）開頭、結尾的字，有幾個？
// queries[i] 裡 [left, right] 對應 words[left]...words[right] 範圍內「合格」的字
class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        unordered_set<char> vowel; // 利用 unordered_set 快速確認「字母是不是母音」
        vowel.insert('a');
        vowel.insert('e');
        vowel.insert('i');
        vowel.insert('o');
        vowel.insert('u');
        int prefixSum[words.size()+1]; // 利用 prefix sum 來記錄「累積」合格的「字數」
        prefixSum[0] = 0;
        for(int i=0; i<words.size(); i++) {
            int N = words[i].length(); // 怕下面那行太長，所以用 N 對應 字串 words[i] 的長度
            if(vowel.count(words[i][0])>0 && vowel.count(words[i][N-1])>0) { // 頭尾是母音
                prefixSum[i+1] = prefixSum[i] + 1; // 利用 prefix sum 技巧，知道「累積」合格的字數
            } else { // 不合格
                prefixSum[i+1] = prefixSum[i]; // 就不用增加，照舊
            }
        }
        vector<int> ans(queries.size());
        for(int i=0; i<queries.size(); i++) {
            int left = queries[i][0], right = queries[i][1];
            ans[i] = prefixSum[right+1] - prefixSum[left]; // 利用「減法」省掉1層迴圈
        }
        return ans;
    }
};

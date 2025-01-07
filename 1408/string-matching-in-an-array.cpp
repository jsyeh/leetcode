// LeetCode 1408. String Matching in an Array
// words 裡，若某字是另一個字的 substring，就放到答案裡（順序沒關係）
class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> ans;
        for(string word : words) {
            for(string word2 : words) {
                if(word != word2 && word2.find(word) != string::npos) {
                    ans.push_back(word);
                    break;
                }
            }
        }
        return ans;
    }
};

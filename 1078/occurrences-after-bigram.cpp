// LeetCode 1078. Occurrences After Bigram
// Bi-gram 是二元組，如果 first 接 second 再接 third 的話，third 是答案
class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        stringstream ss(text); // 可模仿 cin >> word 變 ss >> word
        string word1, word2, word3; // 用來裝「相連」的3個 word
        ss >> word1; // 先讀入第1個字
        ss >> word2; // 先讀入第2個字
        vector<string> ans; // 用來裝答案
        while(ss >> word3){ // 若能讀入第3個字
            // 符合條件，就把第3個字，加到 ans 裡
            if(word1==first && word2==second) ans.push_back(word3);
            word1 = word2; // 接棒：老大換人當
            word2 = word3; // 接棒：老二換人當
        }
        return ans;
    }
};

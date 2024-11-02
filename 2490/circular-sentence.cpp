// LeetCode 2490. Circular Sentence
// 頭尾壓韻的意思：相鄰字的字母要相同，頭尾字（繞圈後）也相同。不相同，就失敗
class Solution {
public:
    bool isCircularSentence(string sentence) {
        if(sentence[0] != sentence[sentence.length()-1]) {
            return false; // 不相同，就失敗
        }

        stringstream ss(sentence);
        string word0, word1;
        ss >> word0;
        while(ss >> word1) {
            // 不相同，就失敗
            if(word0[word0.length()-1] != word1[0]) return false;
            word0 = word1;
        }
        return true;
    }
};

// LeetCode 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
// 找一下 searchWord 是否在 sentence 裡有出現在字首
class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        stringstream ss(sentence); // 轉成 stringstream 方便 ss >> word
        string word;
        int L = searchWord.length(); // 字的長度，方便取 substr(0,L)
        for(int t=1; ss >> word; t++) { // 逐字斷字、分析（從1開始）
            if(searchWord == word.substr(0,L)) return t; // 找到答案
        }
        return -1; // 沒找到答案
    }
};

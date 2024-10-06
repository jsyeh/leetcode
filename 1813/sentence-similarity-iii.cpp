// LeetCode 1813. Sentence Similarity III 兩句子「是否相似」，即只差「插入一段句子」
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        vector<string> words1, words2;  // 用來將2個句子「斷開」
        stringstream ss1(sentence1), ss2(sentence2);  // 很像 cout >> word 很好用
        string word;  // 供 stringstream 讀入
        while(ss1>>word) words1.push_back(word);  // 會以空格斷開，再插入 words 裡
        while(ss2>>word) words2.push_back(word);

        int N1 = words1.size(), N2 = words2.size();
        int i = 0, j = 0;  // 左邊i個word相同、右邊j個word相同
        while(i<N1 && i<N2 && words1[i]==words2[i]) i++;
        while(j<N1-i && j<N2-i && words1[N1-1-j]==words2[N2-1-j]) j++;
        // 上面 N1-i 和 N2-i 很巧妙，可避開左邊i個「比對成功」的字
        if(i+j==N1 || i+j==N2) return true;  // 能湊出其中一個字，就太好了
        return false;
    }
};

// LeetCode 1592. Rearrange Spaces Between Words
// 重新調整「字與字之間」的「空格數量」
class Solution {
public:
    string reorderSpaces(string text) {
        int N = text.length();
        stringstream ss(text);
        string word;
        vector<string> words;
        int S = N; // total space 想計算「有幾個空格」
        while ( ss >> word ) {
            words.push_back(word);
            S -= word.length();
        } // 扣掉有字的部分，就會剩下空格的數量
        string ans = words[0]; // 第1個字先放入
        if (words.size()-1==0) { // 若只有1個字
            for (int k=0; k<S; k++) ans += ' '; // 就把空白都放後面
            return ans;
        }
        string space;
        int avgS = S / (words.size()-1); // 字間要放幾個空格
        for (int k=0; k<avgS; k++) space += ' '; // 湊齊「字間空白」
        for (int i=1; i<words.size(); i++) {
            ans += space + words[i];
        }     // 字間空白 + 下一個字
        int tailS = S - avgS*(words.size()-1); // 最後的空白
        for (int k=0; k<tailS; k++) ans += ' ';
        return ans;
    }
};


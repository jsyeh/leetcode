bool cmp(string a, string b) {  // 自製的比較函式
    // 長度相同時，小的字母在左邊
    if(a.length()==b.length()) return b.compare(a) > 0; 
    return a.length() > b.length(); //希望從「長到短」
}
class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        sort(dictionary.begin(), dictionary.end(), cmp);
        for(string word : dictionary) {
            int k = 0;//word[k] vs. s[i]
            for(int i=0; i<s.length(); i++) {  // 逐字母比較，是否合格
                if(k<word.length() && s[i] == word[k]) k++;
            }
            if(k==word.length()) return word;
        }
        return "";
    }
};

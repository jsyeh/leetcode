// LeetCode 1880. Check if Word Equals Summation of Two Words
// 把 'a'...'j' 變成 0...9, 「字串」就能變成10進位數字。看加法是否正確。
class Solution {
public:
    int s2i(string word) { // string to integer
        int ans = 0;
        for(int i=0; i<word.length(); i++){
            ans = ans * 10 + word[i] - 'a';
        } // 逐字把字母變成數字，再接成10進位數字
        return ans;
    }
    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        return s2i(firstWord) + s2i(secondWord) == s2i(targetWord);
        // 題目想測是否成立，就用 == 來檢查即可
    }
};

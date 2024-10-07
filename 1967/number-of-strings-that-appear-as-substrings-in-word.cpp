// LeetCode 1967. Number of Strings That Appear as Substrings in Word
// 問 pattern 裡，有幾個是 word 的子字串
class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int ans = 0;
        for(string s : patterns){
            if(word.find(s) != string::npos) ans ++;
        }
        return ans;
    }
};

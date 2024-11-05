// LeetCode 293. Flip Game
// 請在 currentState 裡，挑任意2個相連的++ 變 --
// 把全部的可能，都放入 ans 裡
class Solution {
public:
    vector<string> generatePossibleNextMoves(string currentState) {
        string s = currentState;
        vector<string> ans;
        for(int i=0; i<s.length()-1; i++) {
            if(s[i]==s[i+1] && s[i]=='+') {
                s[i] = s[i+1] = '-';
                ans.push_back(s);
                s[i] = s[i+1] = '+';
            }
        }
        return ans;
    }
};

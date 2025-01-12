// LeetCode 678. Valid Parenthesis String
class Solution {
public:
    bool checkValidString(string s) {
        int d1 = 0, d2 = 0;
        for(char c : s) {
            if(c=='*') {
                d1++;
                d2--;
            } else if(c=='(') {
                d1++;
                d2++;
            } else { // c==')'
                d1--;
                d2--;
            }
            if(d1<0) return false;
            if(d2<0) d2 = 0;
        }
        if(d2==0) return true;
        return false;
    }
};

// LeetCode 58. Length of Last Word
class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        string last;
        int ans = 0;
        while(getline(ss, last, ' ')){
            int len = last.length();
            if(len!=0) ans = len;
        }
        return ans;
    }
};

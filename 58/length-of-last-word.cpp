class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        int state = 0;//0:nothing, 1: word
        for(int i=0; i<s.length(); i++) {
            if(state==0 && isAlpha(s[i])) {
                state = 1;
                len = 1;
            }else if(state==1 && isAlpha(s[i])) {
                len++;
            }else if(state==0 && !isAlpha(s[i])) {

            }else if(state==1 && !isAlpha(s[i])) {
                state = 0;
            }
        }
        return len;
    }
    bool isAlpha(char c) {
        if(c>='A' && c<='Z') return true;
        if(c>='a' && c<='z') return true;
        return false;
    }
};

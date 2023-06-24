class Solution {
public:
    char findTheDifference(string s, string t) {
        int H1[256]={}, H2[256]={};
        for(int i=0; i<s.length(); i++) {
            H1[s[i]]++;
        }
        for(int i=0; i<t.length(); i++) {
            H2[t[i]]++;
        }
        for(char i='a'; i<='z'; i++) {
            if(H1[i]!=H2[i]) return i;
        }
        return 'z';
    }
};

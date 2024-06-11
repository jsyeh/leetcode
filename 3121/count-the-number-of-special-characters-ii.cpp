// 問在 word 裡，有哪些字母，同時有大寫、小寫，而且「小寫全部在大寫前面」
class Solution {
public:
    int numberOfSpecialChars(string word) {
        int H1[26]={}, H2[26]={}; //大寫、小寫 出現次數
        int state[26] = {}; //0:沒出現過，1:正在小寫，2:正在大寫，3:失敗
        for(int i=0; i<word.length(); i++){
            char c = word[i];
            if(c>='a' && c<='z') {
                int ii = c-'a';
                if(state[ii]==0 || state[ii]==1) {
                    H2[c-'a']++;
                    state[ii] = 1;
                } else state[ii] = 3;
            } else if(c>='A' && c<='Z') {
                int ii = c-'A';
                if(state[ii]==1 || state[ii]==2) {
                    H1[c-'A']++;
                    state[ii] = 2;
                } else state[ii] = 3;
            }
        }
        int ans = 0;
        for(int i=0; i<26; i++){
            if(H1[i]>0 && H2[i]>0 && state[i]==2) ans++;
        }
        return ans;
    }
};

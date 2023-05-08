class Solution {
public:
    int longestPalindrome(string s) {
        int H[52]={};
        for(int i=0; i<s.length(); i++){
            char c = s[i];
            if(c>='A' && c<='Z') H[c-'A']++;
            if(c>='a' && c<='z') H[c-'a'+26]++;
        }

        int ans = 0, odd = 0;
        for(int i=0; i<52; i++){
            if(H[i]%2==1) odd++;
            ans += H[i]/2*2;
        }
        if(odd>0) ans++;
        return ans;
    }
};

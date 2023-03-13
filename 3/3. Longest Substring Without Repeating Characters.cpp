class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 1;
        if(s.length()==0) ans=0;
        for(int i=0; i<s.length(); i++){
            int now=0;
            int ascii[256]={};
            for(int j=i; j<s.length(); j++){
                char c = s.at(j);
                if(ascii[c]!=0)break;
                now++;
                ascii[c]++;
            }
            if(now>ans) ans = now;
        }
        return ans;
    }
};

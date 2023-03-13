class Solution {
public:
    string longestPalindrome(string s) {
        int ans=1, start=0, end=1;
        int N = s.length();
        //test even version
        for(int i=0; i<N; i++){
            int len=0; //central i is in the left
            for(int m=1; i-m+1>=0 && i+m<N; m++){
                if(s[i-m+1]==s[i+m]) len+=2; 
                else break;
            }
            if(len>ans){
                ans=len;
                start=i-len/2+1;
                end=i+len/2+1;
            }
        }
        //test odd version
        for(int i=0; i<N; i++){
            int len=1;
            for(int m=1; i-m>=0 && i+m<N; m++){
                if(s[i-m]==s[i+m]) len+=2;
                else break;
            }
            if(len>ans){
                ans=len;
                start=i-len/2;
                end=i+len/2+1;
            }
        }
        return s.substr(start, ans);
    }
};

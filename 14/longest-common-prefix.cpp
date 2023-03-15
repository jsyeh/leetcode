class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int N = strs.size();
        if(N==1) return strs[0];
        int len = strs[0].length();
        for(int i=1; i<N; i++){
            if(len<strs[i].length()) len=strs[i].length();
        }

        int ans=0;
        for(int k=0; k<len; k++){
            int bad=0;
            for(int i=0; i<N; i++){
                if(strs[i][k]!=strs[0][k]){
                    bad=1;
                    break;
                }
            }
            if(bad==1)break;
            ans++;
        }
        return strs[0].substr(0, ans);
    }
};

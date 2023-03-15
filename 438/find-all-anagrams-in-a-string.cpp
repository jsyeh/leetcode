class Solution {
public:
    int H1[26]={};
    int H2[26]={};
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        int N1 = p.length();
        for(int i=0; i<N1; i++){
            H1[ p[i]-'a' ]++;
        }

        int N2 = s.length();
        if(N2<N1) return ans;
        for(int i=0; i<N1; i++){
            H2[ s[i]-'a' ]++;
        }
        if(checkHistogram()) ans.push_back(0);
        for(int i=N1; i<N2; i++){
            H2[ s[i-N1]-'a' ]--;
            H2[ s[i]-'a' ]++;
            if(checkHistogram()) ans.push_back(i-N1+1);
        }
        return ans;
    }
    bool checkHistogram(){
        for(int i=0; i<26; i++){
            if(H1[i]!=H2[i]) return false;
        }
        return true;
    }
};

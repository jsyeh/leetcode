class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        int N = words.size();
        for(int i=N-1; i>=1; i--){
            if(isAnagrams(words[i], words[i-1])) {
                words.erase(words.begin()+i);
            }

        }
        return words;
    }
    bool isAnagrams(string a, string b) {
        int H1[26]={}, H2[26]={};
        int N1=a.length(), N2=b.length();
        if(N1!=N2) return false;
        for(int i=0; i<N1; i++){
            H1[a[i]-'a']++;
            H2[b[i]-'a']++;
        }
        for(int i=0; i<26; i++){
            if(H1[i]!=H2[i])return false;
        }
        return true;
    }
};

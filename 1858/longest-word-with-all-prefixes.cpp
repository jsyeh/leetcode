class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        string ans;
        unordered_set<string> prefix;
        for(string w : words) {
            if(w.length()==1 || prefix.count(w.substr(0,w.length()-1))>0) {
                prefix.insert(w);
                if(w.length()>ans.length()) ans = w;
            }
        }
        return ans;
    }
};

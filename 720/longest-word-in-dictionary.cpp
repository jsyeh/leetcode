class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());  // 照字母排序
        unordered_set<string> prefix;  // 用來存「合理的prefix」
        string ans;
        for(string s : words) {  // 照順序取出 s
            // 長度為1可行 or 有「少1個字母的 prefix」可行
            if(s.length()==1 || prefix.count(s.substr(0,s.length()-1))>0 ) {
                prefix.insert(s); // 把可行的字，也加入 prefix
                if(s.length() > ans.length()) ans = s;  // 更新答案
            }
        }
        return ans;
    }
};

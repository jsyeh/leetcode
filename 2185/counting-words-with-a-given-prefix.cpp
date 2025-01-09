// LeetCode 2185. Counting Words With a Given Prefix
// 給字串 pref，在 words 裡，找有幾個字串的字首與 pref 相同
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int ans = 0;
        int L = pref.length(); // 字串的長度
        for(string word : words) { // 每個字都去測
            if(pref.length() > word.length()) continue; // 長度不夠，換下一個
            if(pref == word.substr(0,L)) ans++; // 如果符合，就又找到1個字了！
        }
        return ans;     
    }
};

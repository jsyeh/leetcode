// LeetCode 2914. Minimum Number of Changes to Make Binary String Beautiful
// 給 '0' '1' 的字串，要能切割成許多「長度偶數、全1或全0」的小字串。
// 那要改變幾個字母呢？「兩兩一組」必須相同，所以不同時，要「換其中1個」即可
class Solution {
public:
    int minChanges(string s) {
        int ans = 0;
        for(int i=0; i<s.length(); i+=2) {
            if(s[i]!=s[i+1]) ans++;
        }
        return ans;
    }
};

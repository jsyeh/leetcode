// LeetCode 3330. Find the Original Typed String I
// 可能有1個字母「重覆按很多次」，問「原本要打的字」有幾種可能
class Solution {
public:
    int possibleStringCount(string word) {
        int ans = 1; // 原本的字都沒按錯，就是1種可能
        for(int i=0; i<word.length()-1; i++) {
            if(word[i]==word[i+1]) ans++;
        }
        return ans;
    }
};

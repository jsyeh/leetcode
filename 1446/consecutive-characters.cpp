// LeetCode 1446. Consecutive Characters
// 字串 s 裡，相同字母連續最長的長度
class Solution {
public:
    int maxPower(string s) {
        int prevN = 1, ans = 1;
        char prevC = s[0];
        for(int i=1; i<s.length(); i++) {
            if(s[i]==prevC) {
                prevN++;
                ans = max(ans, prevN);
            } else {
                prevC = s[i];
                prevN = 1;
            }
        }
        return ans;
    }
};

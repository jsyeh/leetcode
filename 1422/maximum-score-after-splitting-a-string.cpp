// LeetCode 1422. Maximum Score After Splitting a String
// 字串 s 裡有一堆 0 和 1，把它分「左右」兩半，左邊0的個數 + 右邊1的個數，合起來要最多。
class Solution {
public:
    int maxScore(string s) {
        int ans = 0, left0 = 0, right1 = 0; // 左邊0 和 右邊1
        for(int i=0; i<s.length(); i++) { // 先全部算到右邊
            if(s[i]=='1') right1++; // 先統計「右邊1」有幾個
        }
        for(int i=0; i<s.length()-1; i++) { // 再來，逐步增加「左邊」
            if(s[i]=='0') left0++; // 左邊多個1
            else if(s[i]=='1') right1--; // 右邊少個0
            ans = max(ans, left0 + right1);
        }
        return ans;
    }
};

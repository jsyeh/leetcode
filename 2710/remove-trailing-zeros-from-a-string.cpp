// LeetCode 2710. Remove Trailing Zeros From a String
// 把 num 右邊的0刪光光。
class Solution {
public:
    string removeTrailingZeros(string num) {
        for(int i=num.length()-1; i>=0; i--) {
            // 只要字母「不是'0'」就中斷迴圈，。右邊裁掉，當成答案
            if(num[i]!='0') return num.substr(0,i+1);
        }
        return "";  // 只是寫好玩的，應不會變成這樣啦（0都被裁光）
    }
};

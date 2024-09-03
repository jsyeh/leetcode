// LeetCode 2544. Alternating Digit Sum
// 每位數拆開、正、負交錯，加起來。
class Solution {
public:
    int alternateDigitSum(int n) {
        int sign = +1, ans = 0;
        for(char c : std::to_string(n)){
            ans += sign * (c-'0');
            sign *= -1;
        }
        return ans;
    }
};

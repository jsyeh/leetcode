// LeetCode 2259. Remove Digit From Number to Maximize Result
// 在 number 裡，要刪掉1個 digit，問刪完後「最大的數」是什麼
// 其實就看看「刪掉之後」的數，誰比較大。
class Solution {
public:
    string removeDigit(string number, char digit) {
        string ans = "";
        for(int i=0; i<number.length(); i++) {
            if(number[i]==digit) {
                string now = number.substr(0,i) + number.substr(i+1,number.length());
                if(now.compare(ans)>0) ans = now;
            }
        }
        return ans;
    }
};

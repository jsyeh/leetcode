// LeetCode 13. Roman to Integer 羅馬數字 變成 int
class Solution {
public:
    int Table(char c) { // 字母的對照表, 很簡單
        if (c=='I') return 1; // 把所有的字母,都變數字
        if (c=='V') return 5;
        if (c=='X') return 10;
        if (c=='L') return 50;
        if (c=='C') return 100;
        if (c=='D') return 500;
        if (c=='M') return 1000;
        return 0;
    }
    int romanToInt(string s) {
        int ans = 0; 
        int prev = 2000; // 一定不會相同、更大的數字 (擔心「倒裝句」)
        for (int i=0; i<s.length(); i++) {
            //ans += Table( s[i] ); // 把字母 s[i] 丟入 Table()函式 // 先寫錯誤的版本
            // 這是錯誤的版本, 答案會太大, 因為「如果有倒裝句」就會反過來
            int now = Table( s[i] ); // 現在的位數
            if (prev < now) ans = ans + now - prev - prev; // 倒裝句發生了!!!!! 變成減法
            else ans += now; // 正常的句子, 直接加法
            prev = now; // 現在的數字, 變成前一項, 
        } // 現在變成「正確版本亅了
        return ans;
    }
};

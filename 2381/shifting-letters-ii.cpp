// LeetCode 2381. Shifting Letters II
// 給你字串 s，接下來「把某段」往上撥0 or 往下撥1，問最後的字串是什麼
class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        vector<int> sh(s.length()+1); // 用來記錄 shift 的累積改變量
        for(auto shift : shifts) {
            int start = shift[0], end = shift[1], d = shift[2];
            if(d==0) d = -1; // 0 對應「往上播」
            sh[start] += d; // 開始撥
            sh[end+1] -= d; // end+1 的地方，再撥回來
        }
        int d2 = 0;
        for(int i=0; i<s.length(); i++) {
            d2 += sh[i]; // 更新「累積改變量」
            s[i] = ((s[i] - 'a' + d2) % 26 + 26) % 26 + 'a'; // 換算新的字母
        }
        return s;
    }
};

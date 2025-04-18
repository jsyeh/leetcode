// LeetCode 38. Count and Say // 數字連續出現, 就模依RLE方法「編碼」成「數字+字母」的形式
class Solution {
public:
    string countAndSay(int n) {
        if(n==1) return "1";
        string prev = countAndSay(n-1); // 函式呼叫函式
        string ans = "";
        char prevC = prev[0]; // 前一個字母
        int prevN = 1; // 前一個字母,累積出現幾次
        for(int i=1; i<prev.length(); i++){
            if(prevC == prev[i]) prevN++; // 相同, 就+1
            else{ // 字母不相同時
                ans +=  string(to_string(prevN)) + prevC; // 出現幾次 + 哪個字母(送出之前累積的字母)
                prevC = prev[i]; // 新的字母
                prevN = 1; // 從1開始(新的字母,有1個)
            }
        }
        ans += string(to_string(prevN)) + prevC; // 最後一筆, 也要送出去
        return ans;
    }
};

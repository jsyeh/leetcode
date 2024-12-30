// LeetCode 2466. Count Ways To Build Good Strings
// 每次要加入 zero 個 '0' 或 one 個 '1'，問有幾種方法，可建出「合規定長度」的字串
class Solution {
public:
    int gLow, gHigh, gZero, gOne, MOD = 1000000007; //（因數字太大，要 MOD 10**9+7）
    int helper(int i, vector<int>& table) {
        if(i==gHigh) return 1;
        if(i>gHigh) return 0;
        if(table[i]!=-1) return table[i];
        int now = helper(i+gZero,table) + helper(i+gOne,table);
        if(i<gLow) table[i] = now % MOD;
        else table[i] = (1+now) % MOD;
        return table[i]; // 利用「函式呼叫函式」，配合 Memo table 記錄答案，避免重覆計算、結省時間
    }
    int countGoodStrings(int low, int high, int zero, int one) {
        gLow = low; // 將參數，變成 global 變數，就不用傳參數了
        gHigh = high;
        gZero = zero;
        gOne = one;
        vector<int> table(high+1, -1); // 用來查表的 Memo 功能
        return helper(0, table);
    }
};

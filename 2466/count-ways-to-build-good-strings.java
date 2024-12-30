// LeetCode 2466. Count Ways To Build Good Strings
// 每次要加入 zero 個 '0' 或 one 個 '1'，問有幾種方法，可建出「合規定長度」的字串
class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        long [] table = new long[high+1]; // table[i]表示剛好有i個字母 的排列組合總數
        table[0] = 1;
        for(int i=1; i<=high; i++) {
            if(i-one>=0) table[i] += table[i-one]; // 答案從「前面」再加過來
            if(i-zero>=0) table[i] += table[i-zero]; // 答案從「前面」再加過來
            table[i] %= 1000000007; // 再照題目規定「取 MOD」避免太大
        }
        long ans = 0;
        for(int i=low; i<=high; i++) { // 把「合規定長度」的可能性，都加起來
            ans = (ans + table[i]) % 1000000007;
        }
        return (int)ans;
    }
}

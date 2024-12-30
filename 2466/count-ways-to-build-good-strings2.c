// LeetCode 2466. Count Ways To Build Good Strings
// 每次要加入 zero 個 '0' 或 one 個 '1'，問有幾種方法，可建出「合規定長度」的字串
int countGoodStrings(int low, int high, int zero, int one){
    long long table[high+1]; // 使用 Bottom-Up Dynamic Programming
    //table[i]表示剛好有i個字母 的排列組合總數
    table[0] = 1;
    for(int i=1; i<=high; i++){
        table[i] = 0;
        if(i-one>=0) table[i] += table[i-one]; // 答案從「前面」再加過來
        if(i-zero>=0) table[i] += table[i-zero]; // 答案從「前面」再加過來
        table[i] = table[i] % 1000000007;
    }
    long long ans = 0;    //所以答案是 table[low] 加到 table[high]
    for(int i=low; i<=high;i++){ // 把「合規定長度」的可能，全部加起來
        ans = (ans + table[i]) % 1000000007;
    }
    return (int)ans;
}

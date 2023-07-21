class Solution {
public:
    int numSquares(int n) {
        int table[n+1]; //table[t] 表示能加到 t 的 平方數 的最少值
        table[0] = 0; //不存在數字
        table[1] = 1; //1*1 有一個
        for(int t=0; t<=n; t++) table[t] = t; //用一堆1加起來

        for(int t=2; t<=n; t++) {
            for(int i=2; i*i<=n; i++) {
                if(t-i*i>=0 && table[t-i*i]+1 < table[t]) table[t] = table[t-i*i] + 1;
            }
        }
        return table[n];
    }
};

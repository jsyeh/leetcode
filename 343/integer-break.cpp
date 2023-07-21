class Solution {
public:
    int integerBreak(int n) {
        int table[n+1]; //table[i] 表示 i 可以拆成多個數字時，乘積最大值的答案
        table[0] = 1; //沒辦法拆
        table[1] = 1; //沒辦法拆
        table[2] = 1; //1*1

        for(int i=3; i<=n; i++){ //table[i] 可將 i 拆成 3種
            table[i] = table[i-1]; //第一種拆法: (i-1) vs. 1, 乘起來是 table[i-1]
            for(int k=1; k<i; k++){ //後面有兩種拆法
                int part1 = max(table[k], k); //左半邊: 之前存的值 or k 
                int part2 = max(table[i-k], i-k); //右半邊： 之前存的值 or i-k
                if(part1*part2>table[i]) table[i] = part1 * part2;
            }
        }
        return table[n];
    }
};

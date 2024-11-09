// LeetCode 3133. Minimum Array End
// 陣列大小 n，裡面數字小到大排好。它們全部 AND 的結果是 x ，問陣列裡「最右邊最大的那個數」最小能多小？
// 可用「二進位」來理解！問題等價於：由 x 開始，固定裡面的 1，把0慢慢加大，到第 n-1 個數，是哪個數
// ex. 2進位 0100 得到 0100
//    下一個數   1 得到 0101
//    下一個數  10 得到 0110
class Solution {
public:
    long long minEnd(int n, int x) {
        long long part1 = x, part2 = n-1; // 要把 part2 塞進 part1 的 0 裡面
        // 把「不是1」的0，換成「二進位」(n-1)的對應bit，就知道答案
        for(long long int i=0; i<64; i++){
            if( (part1 & (1L<<i))==0 ){ // 如果 part1 對應的 bit 是 0
                // 小心是 1L 因為要 long long int 的 1
                part1 |= (part2%2 << i); // 拆下 part2 的 bit, 放進對應bit
                part2 /= 2; // 剝皮
            }
        }
        return part1;
    }
};

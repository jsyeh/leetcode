// LeetCode 2429. Minimize XOR
// 兩數 num1 num2 請找 x （與num2有相同的0和1）使 x XOR num1 最小
class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int ans = num1, one1 = 0, one2 = 0;
        while(num1>0 || num2>0) { // 剝皮法，數一數「有幾個1」
            one1 += num1 % 2;
            one2 += num2 % 2;
            num1 /= 2;
            num2 /= 2;
        }
        for(int i=0; i<32; i++) { // 32 位元的整數「從低到高位」處理
            // 若 ans 的 1 和 num2 的 1 數量不同，就要修正
            if(one1>one2 && (ans & (1<<i)) != 0) { // 目前 ans 的 '1' 過多，把「低位數」的1「去掉」
                ans ^= (1<<i);
                one1--; // 現在 ans 裡，少掉1個1
            }
            if(one1<one2 && (ans & (1<<i)) == 0) { // 目前 ans 的 '1' 不夠多，也是放在「低位數」
                ans ^= (1<<i);
                one1++; // 現在 ans 裡，增加1個1
            }
        }
        return ans;
    }
};

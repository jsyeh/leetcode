// LeetCode 2571. Minimum Operations to Reduce an Integer to 0
// 目標：把n變成0，每次可把數字「加減」2的i次方。像 1,2,4,8,16,32,...
// 看到 lee215 的解說，可用 bit 來想：最低1個1的話，就消掉。很多1個的話，就+1大量進位。
class Solution {
public:
    int minOperations(int n) {
        int ans = 0;
        while(n>0) {
            if(n%4==1) { // 最末01表示「只有1個1」，就消掉這個1
                n--;
                ans++; // 要操作1步
            }else if(n%2==0) { // 最末0可以直接消掉它，不用付出代價
                n /= 2;
            }else if(n%2==1) { // 最末很多1，加1就可大量進位
                n++;
                ans++; // 要操作1步
            }
        }
        return ans;
    }
};

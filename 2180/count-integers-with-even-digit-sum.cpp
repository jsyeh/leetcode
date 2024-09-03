// LeetCode 2180. Count Integers With Even Digit Sum
// <=num 的數字中，有幾個「每位數加總」是「偶數」？就暴力測測即可
class Solution {
public:
    int countEven(int num) {
        int ans = 0;
        for(int i=2; i<=num; i++){ // 測「範圍」內全部的數字
            int total = 0, n = i;
            while(n>0){
                total += n%10;
                n /= 10;
            }
            if(total%2==0) ans += 1; // 最後是「偶數」，答案+1
        }
        return ans;
    }
};

// LeetCode 2894. Divisible and Non-divisible Sums Difference
// 給你兩個數字 n 對應 1 ... n 的數, m 要做除法的餘數。return 不整除-能整除
class Solution {
public:
    int differenceOfSums(int n, int m) {
        int num1 = 0, num2 = 0; // 左邊:不整除, 右邊:整除
        for(int i=1; i<=n; i++) {
            if( i%m > 0 ) num1 += i; // 不整除, 加到 num1
            else num2 += i; // 整除, 加到 num2
        }
        return num1 - num2;
    }
};

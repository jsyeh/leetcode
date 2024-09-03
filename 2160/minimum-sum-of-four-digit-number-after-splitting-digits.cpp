// LeetCode 2160. Minimum Sum of Four Digit Number After Splitting Digits
// 有4位數1000-9999，將數字拆開、組成成2個數，問加起來「最小的數」
class Solution {
public:
    int minimumSum(int num) {
        vector<int> a = {num%10, num/10%10, num/100%10, num/1000};
        sort(a.begin(), a.end()); // 把每位數，「小到大」排好
        return a[0]*10 + a[1]*10 + a[2] + a[3];
    } // 直覺：小的放十位數、大的放個位數
};

// LeetCode 3370. Smallest Number With All Set Bits
class Solution {
public:
    int smallestNumber(int n) {
        int N = 0; // 第1步, 先用剝皮法,找到n是「二進位」的幾位數
        while (n>0) {
            n = n / 2; // 剝掉一層皮
            N++; // 多了1個位數(二進位的位數)
        }
        cout << "現在發現 n 是(二進位的)幾位數呢? " << N << "位數\n";
        int ans = 0; // 第2步, 再用迴圈,組合出「全部都是1的二進位的N位數」
        for (int i=0; i<N; i++) {
            ans = ans * 2 + 1;
        }
        return ans;
    }
};

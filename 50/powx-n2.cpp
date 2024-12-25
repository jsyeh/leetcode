// LeetCode 50. Pow(x, n) 
// 使用函式呼叫函式，
class Solution {
public:
    double myPow(double x, long long int n) {
        if(n==0) return 1; //  1 *x *x *x *x
        if(n<0){ // 遇到負的n,那就負負得正, 同時把 x 變成分母
            n = -n;
            x = 1/x; // 因為 x 的 -1 次方, 是 1/x
        }
        double now = myPow(x, n/2); //一半的x相乘
        if(n%2==0) return now * now; // 左一半、右一半, 再相乘
        else return now * now * x; // 奇數個相乘
    }
};

// LeetCode 1137. N-th Tribonacci Number
// 0 1 1 2 4 7 13 24 ... 請問第 n 項的答案是多少?
// C++ 的LeetCode版本 要小心 class Solution{ 和 public: 不能動到。
// 最下面的大括號、分號,也不能動到
class Solution {
public:
    int tribonacci(int n) {
        int a[40] = {0, 1, 1}; //前3項先準備好, 後面的 37 項沒寫, 就都是 0
        for(int i=3; i<=n; i++){
            a[i] = a[i-1] + a[i-2] + a[i-3]; //前3項相加 得到新的項
        }
        return a[n]; //答案要算出第n項
    }
};

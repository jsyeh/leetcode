// LeetCode 1652. Defuse the Bomb
// 拆除炸彈：code[i] 是圓形的密碼，算出新的密碼（加前k項or後k項）
// 有同學點播 sliding window 所以我用 sliding window 再寫一次
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int N = code.size();
        vector<int> ans(N);
        if(k==0) return ans; // 全部都放0
        if(k>0) { // 正的k，將之後 k 項加起來
            for(int kk=1; kk<=k; kk++) { // 先算出 a[0] 項
                ans[0] += code[kk];
            }
            for(int i=1; i<N; i++) { // 用「前一項」來「增減」出答案
                ans[i] = ans[i-1] + code[(i+k)%N] - code[i];
            }
            return ans;
        } else { // 負的k，將之前 k 項加起來
            for(int kk=1; kk<=-k; kk++) { // 先算出 a[0] 項
                ans[0] += code[N-kk];
            }
            for(int i=1; i<N; i++) { //  用「前一項」來「增減」出答案
                ans[i] = ans[i-1] + code[i-1] - code[(i-1+k+N)%N];
            }
            return ans;
        }
    }
};

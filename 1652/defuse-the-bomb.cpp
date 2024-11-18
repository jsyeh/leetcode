// LeetCode 1652. Defuse the Bomb
// 拆除炸彈：code[i] 是圓形的密碼，算出新的密碼（加前k項or後k項）
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int N = code.size();
        vector<int> ans(N);
        if(k==0) return ans; // 全部都放0
        if(k>0) { // 正的k，將之後 k 項加起來
            for(int i=0; i<N; i++) {
                for(int kk=1; kk<=k; kk++) {
                    ans[i] += code[(i+kk)%N];
                }
            }
            return ans;
        } else { // 負的k，將之前 k 項加起來
            for(int i=0; i<N; i++) {
                for(int kk=N+k; kk<N; kk++) {
                    ans[i] += code[(i+kk)%N];
                }
            }
            return ans;
        }
    }
};

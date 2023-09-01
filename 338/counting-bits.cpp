// 給數字 n, 把 0...n 的數，全部用2進位表示後，數有幾個1
// n<=10^5, 所以暴力法，應該還做得出來
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1);
        for(int i=0; i<=n; i++){
            int now = i, one = 0;
            while(now>0){
                one += now%2;
                now /= 2;
            }
            ans[i] = one;
        }
        return ans;      
    }
};

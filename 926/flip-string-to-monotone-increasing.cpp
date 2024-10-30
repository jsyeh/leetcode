// LeetCode 926. Flip String to Monotone Increasing
// 最少需 flip 幾次，才能「前面0、後面1」
// 總之，邊界線在某位置，前面都是0、後面都是1
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int zero = 0, one = 0;
        for(int i=0; s[i]!=0; i++) {
            if(s[i]=='0') zero++;
            else one++;
        }
        int N = zero + one; // 總共的位數
        int ans = N;
        one = 0; //在i的左邊有幾個'1'
        for(int i=0; i<N; i++) { // 若以index i 為分界，左邊0（包含）、右邊1
            if(s[i]=='0') zero--; // 右邊有幾個0
            int now = one+zero; // 左邊都是0
            if(now<ans) ans = now;
            if(s[i]=='1') one++; // 左邊有幾個'1'
        }
        return ans;   
    }
};


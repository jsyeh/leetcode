class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0; // 能賺多少錢
        int prev = prices[0]; // 之前最底的價錢
        for(int p : prices) {
            if(p<prev) prev = p; // 如果現在的錢比之前更便宜，那更新 prev
            if(p-prev>ans) ans = p-prev; // 如果賺的錢可以更多，那更新 ans
        }
        return ans;
    }
};

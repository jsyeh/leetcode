// LeetCode 1833. Maximum Ice Cream Bars
// 悶熱的夏天，要吃冰淇淋。n枝冰淇淋，價錢是 costs[i]，可買幾枝冰淇淋？
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(), costs.end());
        int ans = 0;
        for(int cost : costs) {
            if(coins>=cost) {
                coins -= cost;
                ans++;
            }
        }
        return ans;
    }
};
